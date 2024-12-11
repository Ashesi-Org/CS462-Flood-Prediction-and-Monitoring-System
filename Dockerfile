# Use the official Python image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements and application files into the container
COPY requirements.txt requirements.txt
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 7000

# Define the command to run the application
CMD ["python", "app.py"]
