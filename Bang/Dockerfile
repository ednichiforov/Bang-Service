FROM python:3.9

WORKDIR /usr/src/app

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./entrypoint.sh .

RUN chmod +x entrypoint.sh

COPY . .

EXPOSE 8080

ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]
