# Use an Ubuntu base image
FROM ubuntu:latest

# Install Python, ADB, and other necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip adb python3-venv && \
    rm -rf /var/lib/apt/lists/*

# Set working directory inside the container
WORKDIR /app

# Copy the APKs directory into the Docker image
COPY APKs/teams /app/apks/teams
COPY APKs/admin /app/apks/admin
COPY APKs/cp /app/apks/cp

# Copy the Flask application code into the Docker image
COPY APKs/app.py /app/app.py
COPY APKs/templates /app/templates

# Create a Python virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Flask and other Python dependencies
RUN pip install Flask

# Start the Flask application when the container runs
CMD ["python", "app.py"]
