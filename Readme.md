# Django Resume Builder Backend

This repository contains the backend component of a full-stack resume builder application, built with Django, Python, and MongoDB. It provides RESTful APIs for user authentication, resume management, and data persistence.

**Key Features:**

* **RESTful APIs:** Provides a comprehensive set of APIs for CRUD operations on users and resumes.
* **User Authentication:** Secure login and signup functionality.
* **Resume Management:** APIs for creating, updating, deleting, and retrieving resumes.
* **MongoDB Integration:** Uses MongoDB for flexible and scalable data storage.
* **Dockerized Deployment:** Easily deployed using Docker containers.
* **CI/CD Pipeline:** Automated build and deployment using GitHub Actions and AWS EC2.

**Technologies:**

* **Django:** Python web framework for building robust APIs.
* **Python:** Programming language.
* **MongoDB:** NoSQL database for data storage.
* **Docker:** Containerization platform.
* **AWS EC2:** Cloud computing service for hosting the application.
* **Nginx:** Reverse proxy server.

## Getting Started

### Prerequisites

* Python 3.x
* pip
* MongoDB installed and running.
* Docker (optional, for containerized deployment)

### Local Development

1.  **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    To create `requirements.txt`:

    ```bash
    pip freeze > requirements.txt
    ```

3.  **Run migrations:**

    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

4.  **Create a superuser (for Django admin):**

    ```bash
    python3 manage.py createsuperuser
    ```

5.  **Run the development server:**

    ```bash
    python3 manage.py runserver
    ```

6.  **To create Project and App**

    ```bash
    django-admin startproject django_resume_builder
    django-admin startapp authentication
    ```

7.  **Test the authentication app**

    ```bash
    python manage.py test authentication
    ```

### REST API Endpoints

* **Signup:** `POST /api/auth/signup/`

    * Body: `{ "first_name": "John", "last_name": "Doe", "email": "john.doe@example.com", "password": "securepassword123" }`
* **Login:** `POST /api/auth/login/`
* **Get User by ID:** `GET /api/users/{user_id}/`
* **Update User:** `PUT /api/users/{user_id}/`
* **Create Resume:** `POST /api/resumes/`
* **Update Resume:** `PUT /api/resumes/{resume_id}/`
* **Delete Resume:** `DELETE /api/resumes/{resume_id}/`
* **Get All Resumes:** `GET /api/resumes/`
* **Get Resume by ID:** `GET /api/resumes/{resume_id}/`

### Docker Deployment

1.  **Install Docker:**

    Ensure Docker is installed on your system.

2.  **Build and run the Docker container:**

    ```bash
    docker-compose up --build
    ```

3.  **To stop and remove the container:**

    ```bash
    docker-compose down
    ```

4.  **To remove all docker images**

    ```bash
    docker system prune
    ```

### Pushing to Docker Hub

1.  **Login to Docker Hub:**

    ```bash
    docker login
    ```

2.  **Tag the Docker image:**

    ```bash
    docker tag django_resume_builder-backend antrikshsaini/django_resume_builder-backend:latest
    ```

3.  **Push the image to Docker Hub:**

    ```bash
    docker push antrikshsaini/django_resume_builder-backend:latest
    ```

### CI/CD Pipeline

* **GitHub Actions:**
    * A CI/CD pipeline is implemented using GitHub Actions.
    * The CI phase builds the Docker image and pushes it to Docker Hub.
    * The CD phase deploys the image to an AWS EC2 instance.
    * The CI workflow file is located at `.github/workflows/ci.yml`.
* **AWS EC2 Instance:**
    * An EC2 instance is used to host the application.
    * GitHub Actions self-hosted runners are configured on the EC2 instance for CD.
    * To setup the runner on ec2 instance follow the github instructions after going to settings/actions/runners of the repository.
    * Update the ec2 instance using `sudo apt update` and `sudo apt-get upgrade -y`
    * Run the configuration commands provided by github actions.
    * Run the runner using `./run.sh`
* **Nginx Reverse Proxy:**
    * Nginx is used as a reverse proxy to direct requests on port 80 to the Django application running on port 8000.
    * Install Nginx using `sudo apt install nginx`.
    * Get the container's IP address using `docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_name_or_id>`.
    * Edit the Nginx configuration file at `/etc/nginx/sites-available/default` and add:

        ```nginx
        location / {
            proxy_pass http://<container_ip_address>:8000;
        }
        ```

    * Restart Nginx using `sudo systemctl restart nginx`.

### MongoDB Configuration

Ensure that your MongoDB instance is running and accessible to the Django application. Configure the MongoDB connection settings in your Django project's `settings.py` file.

### Future Improvements

* Implement more robust error handling and validation.
* Add comprehensive unit and integration tests.
* Enhance security measures.
* Optimize database queries for performance.
* Document all API endpoints thoroughly.