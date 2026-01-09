# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Tell Docker to listen on port 8000
ENV PORT=8000
EXPOSE 8000

# The start command
CMD ["python", "app.py"]
