Django REST API - CRUD - supermarket application
===========================

This is a simple REST APIs for supermarket application. This store contains a variety of food, beverages, and household products, organized into various categories. These categories have subcategories and subcategories have items under them. Each item has a price for which it can be sold. This API is able to add, update, view, and delete such records from a database using the Django REST Framework APIs.

## Contents
1. [System deployment using Docker Compose](#system-deployment-using-docker-compose)
2. [System deployment using only Docker](#system-deployment-using-only-docker)
3. [System deployment on the Linux computer](#system-deployment-on-the-linux-computer)
4. [Testing the API](#testing-the-api)
5. [Docker commands](#docker-commands)
   - [See Docker images](#see-docker-images)
   - [See Docker container status](#see-docker-container-status)
   - [Stop Docker container](#stop-docker-container)
   - [Remove Docker image](#remove-docker-image)
   - [Open Docker container bash](#open-docker-container-bash)
   - [List all Docker containers](#list-all-docker-containers)
   - [Delete Docker container using CONTAINER ID](#delete-docker-container-using-container-id)
   - [Delete all Docker containers](#delete-all-docker-containers)



## System deployment using Docker Compose

Just run the following command ```docker compose up``` and the api will be availabe in the endpoint ```http://localhost:8000/todo```

### Build and run

```
docker compose up
```

Or

### Run migrations, build and run
```
docker compose run api python manage.py migrate
docker compose build
docker compose up
```

### Testing the API running on the Docker container

API: http://127.0.0.1:8000/api   

- Create item: http://127.0.0.1:8000/api/create/
  - POST http://127.0.0.1:8000/api/create/
- Search items
  - Search by item name: GET http://127.0.0.1:8000/api/all/?name=item_name
  - Search by category: GET http://127.0.0.1:8000/api/all/?category=category_name
  - Search by subcategory: GET http://127.0.0.1:8000/api/all/?subcategory=category_name
- View items: http://127.0.0.1:8000/api/all/
  - GET http://127.0.0.1:8000/api/all/
- Update item: 
  - PUT http://127.0.0.1:8000/api/update/<pk>/
- Delete item: 
  - DELETE http://127.0.0.1:8000/api/delete/<pk>/

Go back to [Contents](#contents).



## System deployment using only Docker

### Install Docker on Ubuntu

Follow the instructions available on: https://docs.docker.com/engine/install/ubuntu/

### Build the Docker project

#### Using Python 3.7

```
docker build -f Dockerfile_python3 -t django_api_supermarket_application .
```

* Output Dockerfile using ```FROM python:3.7-alpine```

```
=> [internal] load .dockerignore                                                                                                                                                                                         0.3s
 => => transferring context: 2B                                                                                                                                                                                           0.0s
 => [internal] load build definition from Dockerfile_python3                                                                                                                                                              0.5s
 => => transferring dockerfile: 556B                                                                                                                                                                                      0.0s
 => [internal] load metadata for docker.io/library/python:3.7-alpine                                                                                                                                                      1.1s
 => [1/5] FROM docker.io/library/python:3.7-alpine@sha256:...                                                                                                0.0s
 => [internal] load build context                                                                                                                                                                                         0.5s
 => => transferring context: 957.51kB                                                                                                                                                                                     0.3s
 => CACHED [2/5] RUN mkdir /code                                                                                                                                                                                          0.0s
 => CACHED [3/5] WORKDIR /code                                                                                                                                                                                            0.0s
 => CACHED [4/5] COPY . /code/                                                                                                                                                                                            0.0s
 => CACHED [5/5] RUN pip install -r requirements.txt                                                                                                                                                                      0.0s
 => exporting to image                                                                                                                                                                                                    0.0s
 => => exporting layers                                                                                                                                                                                                   0.0s
 => => writing image sha256:...                                                                                                                              0.0s
 => => naming to docker.io/library/django_api_supermarket_application     
```

### To run the Docker container

```
docker run -d -p 8000:8000 django_api_supermarket_application
```

where:

* -p 8080:8000: publish the port 8080 to 8000
* django_api_supermarket_application: name of the docker container

### Testing the API running on the Docker container

API: http://127.0.0.1:8000/api/   

- Create item: http://127.0.0.1:8000/api/create/
  - POST http://127.0.0.1:8000/api/create/
- Search items
  - Search by item name: GET http://127.0.0.1:8000/api/all/?name=item_name
  - Search by category: GET http://127.0.0.1:8000/api/all/?category=category_name
  - Search by subcategory: GET http://127.0.0.1:8000/api/all/?subcategory=category_name
- View items: http://127.0.0.1:8000/api/all/
  - GET http://127.0.0.1:8000/api/all/
- Update item: 
  - PUT http://127.0.0.1:8000/api/update/<pk>/
- Delete item: 
  - DELETE http://127.0.0.1:8000/api/delete/<pk>/

Go back to [Contents](#contents).



## System deployment on the Linux computer

## Installation and setup

1) Create python virtual environment

```
python3 -m venv venv
```

2) Activate python virtual environment

```
source venv/bin/activate
```

3) Install python dependencies

* Upgrade pip

```
python3 -m pip install --upgrade pip
```

* Install python dependencies 
```
pip install -r requirements.txt
```

4) Run Django migrations

```
python manage.py migrate
```

5) Create a Django super user to access the database table using the ```/admin``` URL.

```
python manage.py createsuperuser
```

* Create the admin user (username, email and password)

```
Username: admin 
Email address: admin@gmail.com
Password: <PASSWORD HERE>
Password (again): <PASSWORD HERE>
```

**Note:** To access the ```/admin``` page run the system (```python manage.py runserver```) and open ```http://127.0.0.1:8000/admin```

## Running the API

1) Run the Django system (API)

```
python manage.py runserver
```
2) Open the ```index``` page: 

* Index page: http://127.0.0.1:8000/

3) Open the API

* API-URL: http://127.0.0.1:8000/api

Go back to [Contents](#contents).



## Testing the API

- Create item: http://127.0.0.1:8000/api/create/
  - POST http://127.0.0.1:8000/api/create/
- Search items
  - Search by item name: GET http://127.0.0.1:8000/api/all/?name=item_name
  - Search by category: GET http://127.0.0.1:8000/api/all/?category=category_name
  - Search by subcategory: GET http://127.0.0.1:8000/api/all/?subcategory=category_name
- View items: http://127.0.0.1:8000/api/all/
  - GET http://127.0.0.1:8000/api/all/
- Update item: 
  - PUT http://127.0.0.1:8000/api/update/<pk>/
- Delete item: 
  - DELETE http://127.0.0.1:8000/api/delete/<pk>/

The API can be tested using ```curl``` or tools like [Postman](https://www.postman.com/).

* API-URL: http://127.0.0.1:8000/api

Go back to [Contents](#contents).

### GET and POST using ```curl```

1) [GET] Endpoint to list all items: **API-URL/api/all**

```
curl http://127.0.0.1:8000/api/all/
```

Go back to [Contents](#contents).

2) [POST] Endpoint to create a new item: POST **API-URL/api/create/**

***Note:*** Change the values of "name", "category", "subcategory" and "amount" below before use the ```curl``` command.

```
curl -X POST http://localhost:8000/api/create/ -H "Content-Type: application/json" -d '{"name":"item name 1","category":"category name 1","subcategory":"subcategory name 1","amount":123}'
```

Go back to [Contents](#contents).

3) [PUT] Endpoint to update an item: PUT **API-URL/api/update/pk**

***Note:*** Use the correct item id and change the values of "name", "category", "subcategory" and "amount" below before use the ```curl``` command.

```
curl -X PUT http://localhost:8000/api/update/1 -H "Content-Type: application/json" -d '{"name":"item name 2","category":"category name 2","subcategory":"subcategory name 2","amount":456}'
```

Go back to [Contents](#contents).

4) [DELETE] Endpoint to delete an item: DELETE **API-URL/api/delete/pk**

```
curl -X DELETE http://localhost:8000/api/delete/1
```

## Docker commands

### See Docker images

```
docker images
```

* Output

```
REPOSITORY       TAG       IMAGE ID       CREATED              SIZE
django_project   latest    <>   About a minute ago   167MB
```

### See Docker container status

```
docker ps
```

### Stop Docker container

```
docker ps
docker stop <CONTAINER ID>
```

### Remove Docker image

```
docker images
docker image rm <IMAGE ID> --force
```


### Open Docker container bash

```
docker ps
docker exec -it <CONTAINER id> /bin/bash
```

* Output

```
root@...:/app#

root@...:/app# ls
Dockerfile  README.md  db.sqlite3  manage.py  requirements.txt  todo_api  todo_app

root@...:/app# pwd
/app

root@...:/app# exit
```

### List all Docker containers

```
docker container ls -a
```

### Delete Docker container using CONTAINER ID

```
docker rm <CONTAINER-ID>
```

Go back to [Contents](#contents).

### Delete all Docker containers

```
docker rm $(docker ps -aq)
```

Go back to [Contents](#contents).
