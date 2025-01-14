# Use an official Python runtime as a parent image
FROM python:3.12-slim

COPY ./requirements.txt /

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory in the container
COPY . /sync/repo/

WORKDIR /sync/repo/

# Make port 80 available to the world outside this container
EXPOSE 80

# Run main.py when the container launches
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]