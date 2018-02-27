
FROM python:3.6.4

RUN mkdir app
WORKDIR /code
COPY . /code
RUN pip install --trusted-host pypi.python.org -r /code/requirements.txt

