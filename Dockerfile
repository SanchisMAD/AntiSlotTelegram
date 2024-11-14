# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the bot script into the container
COPY SlotBot.py .

# Run the bot when the container launches
CMD ["python", "SlotBot.py"]