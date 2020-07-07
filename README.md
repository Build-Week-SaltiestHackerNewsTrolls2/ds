# ds Flask app

# Installation

# Setup

```sh
pipenv --python 3.7
```

```sh
pipenv install Flask pandas
```

```sh
pipenv install Flask_SQLAlchemy
```

```sh
pipenv install python-dotenv psycopg2
```

# Usage

```sh
FLASK_APP=saltyapp flask run
```

if you want development mode, this will restart when the code changes
```sh
FLASK_ENV=development FLASK_APP=saltyapp flask run
```


if you have a trouble with wrong env variable from `.env` file
open pipenv shell with `PIPENV_DONT_LOAD_ENV=1 pipenv shell`

# deploying to Herok

```sh
heroku login
heroku create <name_of_app>
```

```sh
pipenv install gunicorn
```

## Add Procfile to run flask applications
