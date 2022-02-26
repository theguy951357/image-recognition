FROM continuumio/miniconda3

ENV FIFTYONE_DATABASE_URI "mongodb://image-recognition-db-1"

COPY . /app
WORKDIR /app

# Required for psutil build
RUN apt-get update -y && apt-get install -y gcc

RUN pip3 install -U pip
RUN conda install psutil
RUN pip3 install fiftyone

RUN conda update conda
RUN conda install tensorflow

RUN eta install models

# Requires an 'images' directory be present in the project root.
# By default, this is standard behavior. Docker compose handles this
# by mapping the host machine's image-recognition/images directory
# to the container's app/images directory.

# The same is true for ./out
CMD ["python3", "src/main.py", "images", "-v"]