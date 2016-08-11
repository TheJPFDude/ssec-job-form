To make this project work, you must first create a virtual 
environment of Python, then install a few extensions.

First, install Flask if you haven't done so (download at 
http://flask.pocoo.org/)

If using a version of Python older than 3.4, you will have to 
download virtualenv.py before creating the virtual environment. If using 
version 3.4 or newer, skip to the paragraph that starts with "For those with..."

On Mac OS X, type this into your terminal: 

$ sudo easy_install virtualenv

On Linux, type: 

$ sudo apt-get install python-virtualenv

On Windows: Download pip first, then type this command into the terminal: 

$ pip install virtualenv

After doing so, type this command into the terminal: 

$ virtualenv flask

For those with versions of Python 3.4 or newer, cd into the info-project folder
and type the following command into the terminal: 

$ python -m venv flask 

(you may need to type python3 instead of python: for example, "python3 -m venv flask")

After creating the virtual environment, enter these commands one by one into
the terminal.


For Linux, OS X, and Cygwin:

$ flask/bin/pip install flask

$ flask/bin/pip install flask-login

$ flask/bin/pip install flask-openid

$ flask/bin/pip install flask-mail

$ flask/bin/pip install flask-sqlalchemy

$ flask/bin/pip install sqlalchemy-migrate

$ flask/bin/pip install flask-whooshalchemy

$ flask/bin/pip install flask-wtf

$ flask/bin/pip install flask-babel

$ flask/bin/pip install guess_language

$ flask/bin/pip install flipflop

$ flask/bin/pip install coverage


For Windows, enter these same commands except instead of flask/bin/pip enter 
flask\Scripts\pip: an example would be 

$ flask\Scripts\pip install flask


Once you have done all of that, the project should work.

Thanks to Miguel Grinberg for his tutorial on Flask, which helped me with
much of the basic framework of this program.
(http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)