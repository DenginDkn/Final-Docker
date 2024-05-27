FROM python:3.10-alpine3.15
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
COPY sshd_config /etc/ssh/
COPY entrypoint.sh ./
RUN apk add openssh \
    && echo "root:Docker!" | chpasswd \
    && chmod +x ./entrypoint.sh \
    && cd /etc/ssh/ \
    && ssh-keygen -A

EXPOSE 8000 2222

ENTRYPOINT [ "./entrypoint.sh" ]