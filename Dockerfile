FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Install MongoDB dependencies and other required packages
RUN apt-get update && apt-get install -y libpq-dev gcc && apt-get clean

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Expose the port the app runs on
EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Command to start the Django server with Gunicorn for Production
CMD ["gunicorn", "django_resume_builder.wsgi:application", "--bind", "0.0.0.0:8000"]
