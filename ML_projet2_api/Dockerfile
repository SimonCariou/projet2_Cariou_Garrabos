FROM debian:latest

RUN apt-get update && apt-get install python3-pip -y && apt-get install curl -y

WORKDIR /home/api

COPY ./app/requirements.txt /home/api/requirements.txt
RUN pip3 install -r /home/api/requirements.txt

COPY ./app/utils/install_dependencies.py /home/api/install_dependencies.py
RUN python3 install_dependencies.py

COPY app/ /home/api/app

EXPOSE 8000

ENTRYPOINT ["uvicorn"]

CMD ["app.main:api", "--host", "0.0.0.0"]