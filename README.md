# twitter
<b>Installation Instruction</b>
1.  cd twitter/master

2.
//create a virtualenv 
    In windows
    C:\Users\Name\twitter-master> python -m venv myvenv
    In ubuntu
    $ python3 -m venv myvenv
    
3.
//Start your virtual environment by running:
    In windows
    C:\Users\Name\twitter-master> myvenv\Scripts\activate
    In ubuntu
    $ source/myvenv/bin/activate
 4.
 //Installing packages with requirements
    Ubuntu
    pip install -r requirements.txt
    Windows
    C:\Users\Name\twitter-master> python -m pip install -r requirements.txt
  
  
 5. 
 // Apply migrations
    (myvenv) ~/twitter-master$ python manage.py migrate
 6.
 // run server
    (myvenv) ~/twitter-master$ python manage.py runserver
    
