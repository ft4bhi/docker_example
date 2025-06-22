# Use a slim version of the official Python 3.9 image as the base
FROM python:3.9-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy all files from the current directory on the host to /app in the container
COPY . .

# Install Python dependencies from requirements.txt, without caching to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Inform Docker that the container will listen on port 5000 (for documentation only)
EXPOSE 5000

# Define the command to run when the container starts
CMD ["python", "app.py"]
