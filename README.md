# BlogProject

A blog website built using the Django framework and Python programming language. The website is designed to allow users to post articles and write comments, but only if they are logged in.

Link for Live Demo: [BlogProject](https://blogproject1.pythonanywhere.com/)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you can run the application, you need to have the following software installed:

- Python 3.x
- pip

### Installing

Follow the steps below to set up the project on your local machine:

1. Clone the repository:


``` bash
git clone https://github.com/sobirjonovme/BlogProject.git
```


2. Change into the project directory:

``` bash
cd BlogProject
```


3. Create a virtual environment:

``` bash
python -m venv env
```

 
4. Activate the virtual environment (Linux):

``` bash
source env/bin/activate  # for linux
env/scripts/activate  # for windows
```


5. Install the required packages:

``` bash
pip install -r requirements.txt
```


6. Run the database migrations:

``` bash
python manage.py migrate
```


7. Create a superuser to get access to admin panel:
``` bash
python manage.py createsuperuser
```


8. Run the development server:

``` bash
python manage.py runserver
```


The application should now be running at `http://localhost:8000/`.

## Built With

- [Django](https://www.djangoproject.com) - The web framework used
- [Whitenoise](http://whitenoise.evans.io/en/stable/) - Used for static file serving
- [Python](https://www.python.org) - The programming language used

## Contributing

If you would like to contribute to this project, please submit a pull request.

## Author

- [sobirjonovme](https://github.com/sobirjonovme)
