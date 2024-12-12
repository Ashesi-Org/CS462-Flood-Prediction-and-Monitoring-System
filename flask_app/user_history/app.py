from flask import Flask, jsonify, request
from prometheus_client import Counter, generate_latest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, UserHistory
import os

# =====================
# Flask App Initialization
# =====================
app = Flask(__name__)

# =====================
# Prometheus Metrics Setup
# =====================
REQUEST_COUNT = Counter(
    'api_requests_total', 'Total API Requests', ['method', 'endpoint']
)
USER_ACTION_COUNT = Counter(
    'user_actions_total', 'Total User Actions', ['user_id', 'action']
)

# =====================
# Database Setup
# =====================
DATABASE_URL = os.getenv(
    'DATABASE_URL', 'mysql+pymysql://root:6972dk@localhost/Weatherman'
)
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Ensure all tables defined in models.py are created
Base.metadata.create_all(engine)

# =====================
# Utility Functions
# =====================
def log_user_action(user_id, action, details=None):
    """
    Logs user actions in the database and updates Prometheus metrics.
    """
    try:
        new_action = UserHistory(user_id=user_id, action=action, details=details)
        session.add(new_action)
        session.commit()
        USER_ACTION_COUNT.labels(user_id=user_id, action=action).inc()
    except Exception as e:
        session.rollback()
        raise Exception(f"Error logging user action: {e}")


# =====================
# API Endpoints
# =====================
@app.route('/')
def home():
    """
    Home endpoint providing API documentation.
    """
    return jsonify({
        "message": "Welcome to the User History API",
        "endpoints": [
            {"GET": "/user_history - Fetch user history"},
            {"POST": "/user_history/log - Log a user action"},
            {"GET": "/metrics - Prometheus metrics"}
        ]
    }), 200


@app.route('/user_history', methods=['GET'])
def get_user_history():
    """
    Fetch user history from the database. Optionally filter by user_id.
    """
    REQUEST_COUNT.labels(method='GET', endpoint='/user_history').inc()
    try:
        user_id = request.args.get('user_id')
        query = session.query(UserHistory)
        if user_id:
            query = query.filter(UserHistory.user_id == user_id)
        history = query.all()

        results = [
            {
                'history_id': record.history_id,
                'user_id': record.user_id,
                'action': record.action,
                'action_time': record.action_time.isoformat(),
                'details': record.details
            } for record in history
        ]

        return jsonify({"status": "success", "data": results}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": f"Failed to fetch history: {str(e)}"}), 500


@app.route('/user_history/log', methods=['POST'])
def log_action():
    """
    Log a user action in the database.
    """
    REQUEST_COUNT.labels(method='POST', endpoint='/user_history/log').inc()
    try:
        data = request.json
        user_id = data.get('user_id')
        action = data.get('action')
        details = data.get('details')

        if not user_id or not action:
            return jsonify({"status": "error", "message": "Fields 'user_id' and 'action' are required"}), 400

        log_user_action(user_id, action, details)
        return jsonify({"status": "success", "message": "Action logged successfully"}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": f"Failed to log action: {str(e)}"}), 500


@app.route('/metrics', methods=['GET'])
def metrics():
    """
    Expose Prometheus metrics.
    """
    REQUEST_COUNT.labels(method='GET', endpoint='/metrics').inc()
    return generate_latest(), 200


# =====================
# Application Entry Point
# =====================
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7000)
