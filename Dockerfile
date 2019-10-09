FROM tiangolo/uwsgi-nginx:python3.7
#RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /app/static

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ENV PYTHONPATH=/app

COPY FlaskFrontend /app/FlaskFrontend
COPY App /app/App

COPY uwsgi.ini /app

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/start.sh"]
