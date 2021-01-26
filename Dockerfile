From python:3.7-slim
#From alpine:3.2
Label maintainer = 'neeraj@realbooks.in'

WORKDIR /usr/src/app

COPY Pipfile ./
RUN pip install pipenv
RUN pipenv install

COPY . .
ENV FLASK_APP_MODE=config.ProductionConfig
RUN chmod a+x entrypoint.sh

EXPOSE 22 8080
ENTRYPOINT ./entrypoint.sh

# docker build -t realbooks/realedge .