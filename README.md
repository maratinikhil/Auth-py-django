🐍 Django Project Deployment with Docker (Ubuntu)

A Django web application containerized using Docker and deployed on an Ubuntu server (AWS EC2 or local Ubuntu).

🚀 Features

* Django Web Application
* Dockerized Deployment
* Lightweight Python 3.12 Image
* Easy Setup on Ubuntu Server
* Beginner Friendly Steps

🛠️ Tech Stack

* Python 3.12
* Django
* Docker
* Ubuntu (AWS EC2)
* SQLite / PostgreSQL
* HTML, CSS, JavaScript

📁 Project Structure

Auth-py-django/
│
├── manage.py
├── requirements.txt
├── pydockerfile
├── app/
└── README.md

Prerequisites

* Ubuntu Server (AWS EC2 or local)
* Git installed
* AWS account (if using EC2)


1️⃣ Update System

* sudo apt update

2️⃣ Clone GitHub Repository

* git clone https://github.com/maratinikhil/Auth-py-django.git
cd Auth-py-django

3️⃣ Install Docker (Official Documentation)

* Install Docker from Docker official site:
* https://docs.docker.com/engine/install/ubuntu/

4️⃣ Verify Docker Installation

* docker info

5️⃣ Add User to Docker Group

* sudo usermod -aG docker ubuntu

6️⃣ Verify Docker Again

* docker info

7️⃣ Logout and Login Again

*exit

Login again and check:

* docker info

8️⃣ Create Dockerfile

* vi pydockerfile


9️⃣ Build Docker Image

* docker image build -t pyapp:1.0 -f pydockerfile .

🔟 List Docker Images

* docker image ls

1️⃣1️⃣ Run Docker Container

* docker container run -d -P --name myapp pyapp:1.0

1️⃣2️⃣ Check Running Containers

* docker ps -a

🌍 Access the Application

Open your browser and go to:
* http://<SERVER_PUBLIC_IP>:8000

Admin Panel:

http://<SERVER_PUBLIC_IP>:8000/admin
