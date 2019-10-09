# DraBrIW

Serve rounds to yours friends (and charge them for the favour!)

## Dependencies

You can find them in requirements.txt

Tested on Python 3.7, should work with 3+.

## Setup

Install dependencies with
```shell script
pip install -r requirements.txt
```

## Running

### Clone and run from terminal
Setup the following required environment variables to connect to a database

- MYSQL_HOST
- MYSQL_USER
- MYSQL_PASS
- MYSQL_DB
- (optional) MYSQL_PORT


And then run
```shell script
FLASK_APP=FlaskFrontend:app python -m flask run --host 0.0.0.0
```

### Use docker

```shell script
docker run -d -p 8088:80 \
  --name="drabriw" \
  --env MYSQL_HOST="localhost" \
  --env MYSQL_USER="user" \
  --env MYSQL_DB="database" \
  --env DB_PASS="password" \
  draagc/drabriw
```
And then navigate to http://localhost:8088
