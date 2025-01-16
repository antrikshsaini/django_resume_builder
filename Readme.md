python -m venv <directory>

python3 -m venv venv

source venv/bin/activate

To Create requirements.txt
pip freeze > requirements.txt

using requiremnts.txt
pip install -r requirements.txt

python3 manage.py makemigrations

python manage.py migrate

python3 manage.py createsuperuser

python3 manage.py runserver

to create project
django-admin startproject django_resume_builder

To create APP
django-admin startapp authentication

Test
python manage.py test authentication

Signup body for
http://127.0.0.1:8000/api/auth/signup/

{
"first_name": "John",
"last_name": "Doe",
"email": "john.doe@example.com",
"password": "securepassword123"
}

## Using Docker

install Docker in your system
Run Docker
create environment to run docker-compose and docker commands

### `docker-compose up --build`

### to remove latest created image

docker-compose down

### to delete all images from system

docker system prune

## How to Push Code on Docker Hub Cloud

`docker login`

`docker tag django_resume_builder-backend antrikshsaini/django_resume_builder-backend:latest`

`docker push antrikshsaini/django_resume_builder-backend:latest`

## CI/CD pipeline

Github Action CI/CD pipeline is added
Deployed code on Docker Hub

## Steps to create CI/CD pipeline

Go to Actions on Github
create Docker Image
create .github/workflows/ci.yml

ci.yml will contain CI until Bulid phase

### Deployment Phase

create EC2 instance on AWS
Run AWS instance

Create Github action Runners for CD Pipeline
Go to Runners on settings of Github Repository

Create New Runner
Select Linux

Run all the commands on linux EC2 instance
First update EC2 instance by runnning "sudo apt update"
"sudo apt-get upgrade -y"

After running all commands written on Download part

Run all configure commands

to run on ec2 instance
./run.sh

#### Use this YAML in your workflow file for each job

runs-on: self-hosted

### Install Docker on EC2 instance

Use ubuntu docs to install docker

"sudo docker ps" to check if docker is install properly
