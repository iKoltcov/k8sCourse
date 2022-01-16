FROM ubuntu:focal
RUN apt-get update -y \ 
    && apt-get install -y python3 python3-pip python3-dev build-essential \
    && apt-get clean
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt
COPY . /app
CMD ["/bin/bash", "-c", "python3 /app/hello-world.py"]