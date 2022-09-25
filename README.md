# BookmarkManager-DjangoRESTAPI
A simple bookmark manager CRUD app developed with django-rest framework and postgresql database. Follow the steps to run the project in your local machine.<br>
Step 1: Download this project to your local machine or clone the project using the following git command 

```git clone https://github.com/Borhan-Uddin/BookmarkManager-DjangoRESTAPI.git```

## Run Without Docker 
Step 2: Goto project folder and open terminal/cmd. Run the following command 

```pip install -r requirements.txt ``` 

Step 3: Run following command in the terminal 

```python manage.py runserver ``` 

Step 4: Now open any browser and type `http://127.0.0.1:8000/api/v1/bookmarks/` to access the app. 

## Run with Docker

Step 2: Go to the project folder and open the cmd/terminal. Run the following command. Make sure you have docker installed in your system. If you don't have docker installed click [Docker installation](https://docs.docker.com/get-docker/) and follow the instructions to install docker.<br>

```docker-compose build```

Step 3: Run the app in docker container using the following command 

```docker-compose up```

Step 4: Now open any browser and type `http://127.0.0.1:8000/api/v1/bookmarks/` to access the app. 
