FROM python:3.10-alpine3.15

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

COPY sshd_config /etc/ssh/sshd_config

COPY entrypoint.sh ./
RUN chmod +x ./entrypoint.sh

RUN apk add openssh \
    && echo "root:Docker!" | chpasswd \
    && ssh-keygen -A

EXPOSE 8000 2222

ENTRYPOINT [ "./entrypoint.sh" ]
