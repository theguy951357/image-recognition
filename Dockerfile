FROM tensorflow/tensorflow:latest-gpu

COPY . /app
WORKDIR /app

RUN apt update && apt upgrade -y
RUN apt install -y git ffmpeg
RUN pip install --upgrade pip
RUN pip install fiftyone==0.14.4 && \
    pip install psutil==5.9.0

RUN eta install models

CMD ["python3", "src/main.py", "-v"]