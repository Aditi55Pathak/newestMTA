# Use the official Python image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the app directory to the working directory
COPY . .

# Specify the command to run on container start
CMD ["python", "app.py"]
