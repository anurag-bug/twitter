# Installation Instructions
#
#### 1. Navigate to Source Directory
```sh 
$ cd twitter-master
```

#### 2.Create a virtualenv
In windows
```sh
C:\Users\Name\twitter-master> python -m venv myvenv 
```
In Linux
```sh
$ python3 -m venv myvenv
```

#### 3. Start your virtual environment by running:
In windows
```sh
C:\Users\Name\twitter-master> myvenv\Scripts\activate
```
In ubuntu
```sh
$ source/myvenv/bin/activate
```
#### 4. Installing packages with requirements
Ubuntu
```sh
pip install -r requirements.txt
```
Windows
```sh
C:\Users\Name\twitter-master> python -m pip install -r requirements.txt
  ```
  
#### 5. Apply migrations
```sh
(myvenv) ~/twitter-master$ python manage.py migrate
```
#### 6. Run server
```sh
#### (myvenv) ~/twitter-master$ python manage.py runserver
```
 App will run on http://127.0.0.1:8000/twitter/search/

### Todos

 - Create twitter account specific feedback
 
