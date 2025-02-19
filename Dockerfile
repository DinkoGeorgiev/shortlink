# Dockerfile

# pull the official docker image
FROM python:3.12-slim

# set env variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# set work directory
WORKDIR /code


# install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy project
COPY alembic.ini /code/alembic.ini
COPY migrations /code/migrations
COPY static /code/static
COPY ./app /code/app

# start
CMD ["fastapi", "run", "app/main.py", "--port", "80"]
