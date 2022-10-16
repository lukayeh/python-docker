# Use an official Python runtime as a parent image
FROM python:3-slim

# # Copy the current directory contents into the container at /app
COPY . /app

# # Set the working directory to /app
WORKDIR /app

# # Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt 

# # Run gunicorn.sh when the container launches
ENTRYPOINT ["./gunicorn.sh"]