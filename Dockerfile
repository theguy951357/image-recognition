FROM tensorflow/tensorflow:latest-gpu

COPY . /app
WORKDIR /app

RUN apt install -y git

RUN pip install --upgrade pip
RUN pip install psutil==5.9.0
RUN pip install fiftyone==0.14.4
RUN eta install models

CMD ["python3", "src/main.py", "-v"]