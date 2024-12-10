# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app


# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py .
COPY flood_model.h5 /app/flood_model.h5
COPY flood_model.h5 /app/scaler.pkl

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]

