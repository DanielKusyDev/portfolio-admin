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

# Configure SSH
RUN apt-get install -y openssh-server && echo "root:Docker!" | chpasswd
COPY sshd_config /etc/ssh/

# Copy and configure the ssh_setup file
RUN mkdir -p /tmp
COPY ssh_setup.sh /tmp
RUN chmod +x /tmp/ssh_setup.sh && (sleep 1;/tmp/ssh_setup.sh 2>&1 > /dev/null)
EXPOSE 80 2222

COPY ./pyproject.toml .
COPY ./poetry.lock .
RUN /root/.local/bin/poetry config virtualenvs.create false
RUN /root/.local/bin/poetry install

COPY . .



ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]