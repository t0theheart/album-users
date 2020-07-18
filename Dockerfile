FROM python:3.8

ENV PYTHONPATH=/usr/src/app

WORKDIR /usr/src/app

COPY Pipfile.lock Pipfile ./
RUN pip install -U pip pipenv && pipenv install --system --deploy --ignore-pipfile --dev

COPY . .

EXPOSE 8080

ENTRYPOINT ./entrypoint.sh