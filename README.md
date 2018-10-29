# twitter
<b>Installation Instruction</b><br>
1.  cd twitter-master
<br>
2.
//create a virtualenv <br>
    In windows
    C:\Users\Name\twitter-master> python -m venv myvenv <br>
    In ubuntu
    $ python3 -m venv myvenv
    <br>
3.
//Start your virtual environment by running:<br>
    In windows
    C:\Users\Name\twitter-master> myvenv\Scripts\activate <br>
    In ubuntu
    $ source/myvenv/bin/activate<br>
 4.
 //Installing packages with requirements<br>
    Ubuntu
    pip install -r requirements.txt<br>
    Windows<br>
    C:\Users\Name\twitter-master> python -m pip install -r requirements.txt
  
  
 5. <br>
 // Apply migrations<br>
    (myvenv) ~/twitter-master$ python manage.py migrate
 6.<br>
 // run server<br>
    (myvenv) ~/twitter-master$ python manage.py runserver
    
