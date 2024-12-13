
# **🌊 Flood Prediction and Monitoring System**

The **Flood Prediction and Monitoring System** is a cloud-based web application designed to help predict and monitor flood risks in vulnerable areas, particularly in flood-prone regions of Ghana, like Accra. This system provides crucial insights to help individuals, government agencies, and developers take proactive measures to mitigate the impacts of flooding. Flooding in urban areas often leads to property damage, economic loss, and even loss of life. This project aims to address these challenges by offering accessible, data-driven flood risk assessments.

---

## **🚀 Features**

- **Data Collection**: Real-time collection of rainfall, historical flood events, and environmental factors.
- **Predictive Analysis**: Uses environmental data to calculate flood risks based on recent or forecasted rainfall levels.
- **Location-Specific Insights**: Users can input or view flood risk predictions for specific areas, receiving a risk level overview.
- **User-Friendly Interface**: A cloud-based web app with interactive visualizations and easy navigation for monitoring flood risks.
- **Real-Time Alerts**: Provides instant notifications for high-risk flood zones to ensure timely actions.
- **Scalable Design**: Built using cloud technologies to handle increasing data loads efficiently.

---

## **🔍 How It Works**

The **Flood Prediction and Monitoring System** operates by:

1. **Data Aggregation**: Gathering data from various sources, including rainfall measurements, past flood events, and geographic data.
2. **Predictive Modeling**: Using machine learning models to analyze collected data and predict the likelihood of a flood in specific areas.
3. **User Input and Analysis**: Allows users to input specific location data for customized flood risk insights.
4. **Visualization and Monitoring**: Displays real-time and forecasted flood risk levels for selected regions through interactive charts and maps.
5. **User Tracking**: Tracks user logins, interactions, and navigation patterns for enhanced analytics.

---

## **🛠️ Technologies Used**

- **Frontend**: HTML, CSS, JavaScript for interactive data visualization.
- **Backend**: Python with Flask to handle web application logic and data processing.
- **Machine Learning**: Scikit-Learn, TensorFlow for predictive modeling.
- **Database**: MySQL for data storage and retrieval.
- **Cloud Services**: AWS for real-time data access and scalability.
- **Container Infrastructure**: Docker for containerized deployment of the application.
- **User Activity Monitoring**: Prometheus for logging user interactions and system performance.

---

## Project Management

We are using [ClickUp](https://app.clickup.com/9012511042/v/b/4-90122116904-2) as our project management tool to organize tasks and track progress. Below are details of the setup:

### Task Board Overview
![Task Board Overview](images/task_board.png)

### Workflow  
Our workflow follows the Agile methodology, divided into milestones to track progress.  
1. **Milestone Planning**: Each milestone focuses on a specific deliverable. Tasks are created, assigned to team members, and tracked in the project management tool.  
2. **Daily Updates**: Standups via WhatsApp to sync on progress.  
3. **Task Tracking**: We use ClickUp boards to maintain task progress from "To Do" to "In Progress" and "Done."

---

## 📊 Data Sources and Collection

The system relies on multiple data sources to provide accurate flood predictions:

- **Weather Data**: Real-time and historical rainfall data from government agencies and APIs like OpenWeather or Meteostat.
- **Flood History**: Data on past flooding events in the targeted regions.
- **Geographical Information**: Data on elevation, topography, and drainage systems from sources like Google Maps API or GIS databases.

---

## 📈 Machine Learning and Modeling

Flood predictions are made using machine learning algorithms trained on a variety of flood-related environmental data. Models include:

- **Logistic Regression**: Used for binary classification of flood risk.
- **Random Forest**: Used for assessing flood risk probability based on environmental factors.
- **Recurrent Neural Network (RNN)**: For time-series forecasting of rainfall and its potential impacts on flood risks.

---

## 🌩️ Robust Model and Cloud Hosting
![robust_model](https://github.com/user-attachments/assets/4b247b89-aad2-43f4-b0cf-549e6a42d376)



### Model Accuracy
Our local model achieved an outstanding accuracy of **98%**, demonstrating its effectiveness in predicting flood risks.

### Cloud Hosting for Robust Models
Cloud computing plays a critical role in hosting resource-intensive models like the RAG system due to its scalability, flexibility, and cost-efficiency. By leveraging cloud infrastructure, the robust model can efficiently handle high computational and storage demands, ensuring reliable performance and accessibility for users.

The decision to host the system on a different cloud provider underscores the importance of matching resource requirements to the provider's capabilities, including GPU-optimized virtual machines, data storage solutions, and low-latency networking. Additionally, cloud platforms enable seamless integration of diverse data sources and distributed processing of tasks, vital for real-time operations in complex systems like the RAG model.

This approach ensures:
- **High Availability**: Reliable system uptime and accessibility for users.
- **Improved Response Times**: Faster prediction and monitoring capabilities.
- **Dynamic Scaling**: Ability to scale resources based on workload demands.

## **🏗️ Infrastructure Setup**

### **Container Infrastructure**

The system uses a containerized infrastructure to streamline development and deployment. Below is the container setup:

1. **Containers**:
   - `user_tracking` container for logging and tracking user activity.
   - `database` container for managing flood prediction data.
   - `mwin7/landingpage` for the frontend interface.
   - `mwin7/backendlogin` for secure user login management.
  
![containers](https://github.com/user-attachments/assets/7a0de5e0-b5cc-4cde-ab73-f48e2a1b520c)


2. **Images Created**:
   - `evansjunior/flood-prediction-app:latest`: The main application image.
   - `evansjunior/user-prediction-app:latest`: The user tracking application image.

![architecture](https://github.com/user-attachments/assets/a4830b9d-2576-41f1-b0e3-604c9e197d3a)


---

## **🌐 Installation**

Follow these steps to set up the **Flood Prediction and Monitoring System** locally:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/YourUsername/FloodPredictionMonitoring.git
    cd FloodPredictionMonitoring
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure the Environment**:
   - Set up a `.env` file with necessary environment variables, such as API keys for weather data, database configurations, and cloud service credentials.

4. **Run the Application**:
    ```bash
    python app.py
    ```

5. **Access the App**:
    - Visit http://127.0.0.1:5000 to view and interact with the Flood Prediction and Monitoring System.

---

## **🧪 Testing**

We performed rigorous testing to ensure the application runs smoothly and meets all functional requirements:

- **Testing Suite**: Utilized the **Qodo Gen Test Suite** for automated tests of APIs and containerized services.
- **API Testing**: Conducted thorough API response testing using **Postman** to validate endpoints and ensure accurate data handling.

### **Testing Results**

Here are some snapshots of the testing process:

1. **Qodo Gen Test Suite**:  
![qodo_test_suite](https://github.com/user-attachments/assets/d1223629-2cb4-4e2f-a471-7c0fe327f263)


![qodo_test_suite2](https://github.com/user-attachments/assets/3882edac-8940-4dea-bacf-edf930eabfbc)


![qodo_test_suite3](https://github.com/user-attachments/assets/81554a9e-47b3-4f63-b15a-5cf15f11ffbc)

   
   *Detailed output from the Qodo Gen Test Suite highlighting successful API responses.*

3. **Postman Testing**:  
 ![postman_api_testing](https://github.com/user-attachments/assets/0a73bcf1-5a64-4c18-b227-fe4a9714f390)

 ![postman](https://github.com/user-attachments/assets/35287d54-9116-4d53-b0ee-11f16d03a97c)


   *Validation of API endpoints with expected responses and latency checks.*

---

## **📋 Limitations and Future Improvements**

- **Latency**: There is some latency when retrieving API responses. Future work will involve optimizing API response times to ensure seamless user experience.
- **Expanded Data Sources**: Adding more diverse data sources for better prediction accuracy.
- **Real-Time Notifications**: Implementing real-time alert systems for high-risk flood zones.
- **Enhanced Machine Learning Models**: Incorporating deep learning architectures to improve prediction accuracy.

---

## **📊 Data Sources and Collection**

The system relies on multiple data sources to provide accurate flood predictions:

- **Weather Data**: Real-time and historical rainfall data from government agencies and APIs like OpenWeather or Meteostat.
- **Flood History**: Data on past flooding events in the targeted regions.
- **Geographical Information**: Data on elevation, topography, and drainage systems from sources like Google Maps API or GIS databases.

---

## **📈 Machine Learning and Modeling**

Flood predictions are made using machine learning algorithms trained on a variety of flood-related environmental data. Models include:

- **Logistic Regression**: Used for binary classification of flood risk.
- **Random Forest**: Used for assessing flood risk probability based on environmental factors.
- **Recurrent Neural Network (RNN)**: For time-series forecasting of rainfall and its potential impacts on flood risks.
- **Gradient Boosting**: For better handling of imbalanced datasets and complex patterns.

---

## **📊 User Activity Tracking**

The system uses **Prometheus** to track user logins, logouts, pages visited, and time spent on the application. Metrics are analyzed to:
- Enhance the user experience.
- Identify popular features.
- Detect unusual behavior patterns.
- Ensure system performance and scalability.

---

## **👥 Contributing**

We welcome contributions to improve the Flood Prediction and Monitoring System. Here's how you can help:

1. **Fork the Repository**: Create a personal fork of the repository.
2. **Clone Your Fork**:
    ```bash
    git clone https://github.com/Evans-Junior/FloodPredictionMonitoring.git
    ```

3. **Create a Branch**:
    ```bash
    git checkout -b feature/YourFeature
    ```

4. **Commit Changes**:
    ```bash
    git commit -m "Add a descriptive message"
    ```

5. **Push Changes**:
    ```bash
    git push origin feature/YourFeature
    ```

6. **Submit a Pull Request**:
   - Once your changes are ready, submit a pull request to the main repository for review.

---

## **📝 License**

This project is licensed under the Ashesi License - see the [LICENSE](LICENSE) file for details.

---

## **📧 Contact Information**

For further inquiries or support, contact us via email:

**kwakukumi14@gmail.com**

---

