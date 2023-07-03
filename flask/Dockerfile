FROM python:slim

RUN mkdir /app

COPY . /app

WORKDIR /app

RUN pip install -r ./requirements.txt

EXPOSE 5000

CMD ["python3", "app.py" ]


# CMD ["/bin/echo", "Hello world"]
# ENTRYPOINT ["/bin/echo"]
# ENTRYPOINT ["/bin/echo", "Hello world"]

