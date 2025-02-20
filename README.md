# ShortLink

A basic async url shortener service using python fastapi and alpine.js + axios

## Setup

### Configure the database container
*Note, this step is necessary only if the db container provisioned by the supplied docker compose file is used.*

* Copy supplied db.env.example as db.env
* Configure the desired settings

### Configure webapp

* Copy supplied web.env.example as web.env
* Configure the desired settings

## Running the project
*Note: This howto has been tested on Linux. Windows setup may differ*

### Using docker compose

From the project root directory run the following

* Build the containers: `docker compose build`
* Start the containers`docker compose up -d`
* Apply db schema migrations: `docker compose exec web alembic upgrade head`
* In your browser navigate to http://127.0.0.1:8000 or the address where the service has been started if different.


### In a virtual environment

* Create a python virtual environment: `python -m venv .venv`
* Activate the virtual environment: `source .venv/bin/activate`
* Install requirements: `pip install -r requirements.txt`
* Configure db settings to point to your desired PostgreSQL server in `web.env`
* Apply db schema migrations: `alembic upgrade head`
* Start the service: `fastapi run app/main.py`
* In your browser navigate to http://127.0.0.1:8000 or the address where the service has been started if different.

## Docs

Api documentation can be accessed at http://127.0.0.1:8000/api/docs and http://127.0.0.1:8000/api/redoc

## TODOs

* Unit/Integration tests
* Improve UI look and UX
* Add link statistics
* Add link administration password (for delete / modify)
* Add password protected links
* Add "premium" short links support (even shorter/custom links based on supplied pre-purchased codes)
* Check public blacklists before accepting a link target
* Bot/Human check/captcha and rate limiting
* Expiring links (TTL / Inactivity)
