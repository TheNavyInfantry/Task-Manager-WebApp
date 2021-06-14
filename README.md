# Task-Manager-WebApp
This is a Task Manager web app which is written with Python &amp; Flask Framework 

### How To Run
* Install `virtualenv`:
```
$ pip install virtualenv
```

* Open a terminal in the project root directory and run:
```
$ virtualenv env
```

* Then run the command:
```
$ .\env\Scripts\activate
```

* Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```

* Finally start the web server:
```
$ (env) python app.py
```

* This server will start on port 5000 by default. You can change this in `app.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)

[]: https://flasktaskmanagerwebapp.herokuapp.com/

[Click here for the live version]: https://flasktaskmanagerwebapp.herokuapp.com/
