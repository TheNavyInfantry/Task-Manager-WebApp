# Task-Manager-WebApp
This is a Task Manager web app which is written with Python &amp; Flask Framework 

### How To Run
* Install `virtualenv`:
```
$ pip install virtualenv
```

* Open a terminal in the project root directory and run:
```
$ virtualenv venv
```

* Then run the command:
```
$ source venv/bin/activate
```

* Then install the dependencies:
```
$ (venv) pip install -r requirements.txt
```

* Then setup the database:
```
$ (venv) python
    
    >>> from task_manager import db

    >>> db.create_all()
```

* Finally start the web server:
```
$ (venv) python run.py
```

* This server will start on port 5000 by default. You can change this in `run.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
