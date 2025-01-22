# Use the official Python image (change the version as needed)
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install project dependencies if a requirements file exists
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run your script
CMD ["python", "hydro.py"]
