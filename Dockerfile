FROM python:3.8.12

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt install curl
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt update
RUN ACCEPT_EULA=Y apt install -y gcc python3-dev msodbcsql17 mssql-tools unixodbc-dev
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -

COPY ./pyproject.toml .
COPY ./poetry.lock .
RUN /root/.local/bin/poetry config virtualenvs.create false
RUN /root/.local/bin/poetry install

COPY . .

ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]