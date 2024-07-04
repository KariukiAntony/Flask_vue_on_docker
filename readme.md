# <h1 align = "center">Flask Vue On Docker</h1>

![Flask_Vue_Docker](./client/src/assets/flask_vue_docker.png)
<div align="center">

</div>

## Overview 
**Flask Vue on Docker** is a simple yet powerful and production-ready client-server application. This project demonstrates how to create a robust full-stack application using Flask for the backend API, Vue.js for the frontend client, and Nginx as a reverse proxy. Docker is used for both development and production environments. The setup follows clean architecture principles, adheres to a test-driven development (TDD) approach, and integrates a CI/CD pipeline using GitHub Actions where tests must run successfully before the application is deployed.

## Features 
- **Backend Services**: Written in Python using the Flask framework.
- **Frontend**: Built with Vue.js, providing a reactive and dynamic user interface.
- **Nginx**: Used as a reverse proxy to manage and route traffic efficiently.
- **Clean Architecture**: Ensuring the separation of concerns, making the application scalable and maintainable.
- **Test-Driven Development (TDD)**: Tests are written before the code, ensuring high code quality and reliability.
- **CI/CD Pipeline**: Automated testing, building, and deployment using GitHub Actions.

## Prerequisites
- Docker and Docker Compose 

## Getting Started 
1. clone the repository 
```bash 
 $ git clone https://github.com/KariukiAntony/Flask_vue_on_docker.git
 $ cd Flask_vue_on_docker
``` 
2. spin up the containers. Basically, you get to choose between development, staging and production environment. run the following script ot get started.
```bash 
chmod u+x ./local.sh
 ./local.sh
```

## Access the Application
- Development environment
  - frontend: http://localhost:5173
  - backend: http://localhost:5000/api/books

- Staging environment
  - frontend: http://localhost:8000
  - backend: http://localhost:5000/api/books

- Production environment
  - frontend: http://localhost
  - backend: http://localhost/api/books


## CI/CD Pipeline
This project uses GitHub Actions for the CI/CD pipeline.The pipeline includes steps for:

- linting the code to ensure code quality is met
- running tests 
- deploying the application

## Clean Architecture
The project structure follows the clean architecture principles:
- **api**: Contains the API endpoints.
- **tests**: Includes unit and integration tests.

## Contributions
Contributions are welcome! Please fork the repository and create a pull request.