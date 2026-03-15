# Use a slim version of Python for a smaller image size
FROM python:3.11-slim

# Set environment variables
# PREVENT: Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# PREVENT: Python from buffering stdout/stderr (better logging)
ENV PYTHONUNBUFFERED=1

# Create a non-privileged user for security
RUN adduser --disabled-password --gecos "" flaskuser

# Set the working directory
WORKDIR /app

# Install dependencies first (to leverage Docker cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Create the data directory
RUN mkdir -p /app/data && chown -R flaskuser:flaskuser /app/data

# Switch to the non-root user
USER flaskuser

# Expose the port Flask runs on
EXPOSE 5000

# Run the application
# Using 'run.py' as the entry point
CMD ["python", "run.py"]