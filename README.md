 # pre requisite
 ```
    Download the chrome driver and place it on usr/bin directory
    rename .envExample into .env
    provide the username & password
 ```

 # install all dependencies
 ```
    pip install -r requirements.txt
 ```

 # start
 ```
 uvicorn main:app --host 0.0.0.0 --reload 
 ```