# calculate_insurance_test

## This is a technical requirements for this project:
Requirements:
* Implement a REST API service for calculating the cost of insurance depending on the cargo type and rate.
* The cargo type and rate must be loaded from JSON structure
* The service must calculate the cost of insurance for the request using the current tariff. (Downloaded via API)
* The service returns (declared value * rate) depending on the cargo type and date specified in the request.
* The service must be deployed inside Docker.
* Service must be developed via GIT (Readme file with deployment details)
* Data must be stored in a database



### This project was realized with FastApi + Tortoise ORM + Pydantic + PostgreSQL

# Instruction:

* Before the first run, you need to copy .env.dist to new created .env
* If necessary, change the configuration of ports, logins, passwords, etc.
* Download, install and run Docker
* Run "make dev" command in console
* If you have a Windows, then run the command instead of the previous command: docker compose up -d --build


### With the existing .env

* swagger is available http://127.0.0.1:8000/api/docs
* endpoint to create test data for base tariff http://127.0.0.1:8000/api/insurance/tariff/create
* endpoint to calculate insurance http://127.0.0.1:8000/api/insurance/calculate

