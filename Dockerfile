FROM continuumio/anaconda3

ENV FIFTYONE_DATABASE_URI "mongodb://object-recognition-db-1"

COPY . /app
WORKDIR /app

RUN conda update conda
RUN conda upgrade conda
RUN conda install psutil

RUN pip install --upgrade pip

RUN pip install tensorflow
RUN pip install tensorflow-gpu
RUN pip install fiftyone

RUN eta install models

# Requires an 'images' directory be present in the project root.
# By default, this is standard behavior. Docker compose handles this
# by mapping the host machine's image-recognition/images directory
# to the container's app/images directory.

# The same is true for ./out
CMD ["python3", "src/main.py", "-v"]