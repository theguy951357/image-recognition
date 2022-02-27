# Latest LTS
FROM --platform=linux/amd64 ubuntu:latest

# Copy program files
COPY . /app
WORKDIR /app

# Install base utilities
RUN apt update
RUN apt install -y build-essential \
    && apt install -y wget \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

# Install miniconda
ENV CONDA_DIR /opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-Linux-x86_64.sh -O ~/miniconda.sh && \
     /bin/bash ~/miniconda.sh -b -p /opt/conda

# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH
ENV FIFTYONE_DATABASE_URI "mongodb://object-recognition-db-1"

# Setup conda environment
RUN conda create -n object-recognition python=3.9
ENV PATH /opt/conda/envs/object-recognition/bin:$PATH

# Reload the shell
RUN /bin/bash -c "source activate object-recognition"

# Upgrade conda and install necessary packages
RUN conda update conda
RUN conda upgrade conda
RUN conda install psutil

RUN pip install --upgrade pip
RUN pip install --default-timeout=100 -r requirements.txt

# Required for fiftyone to work as the model above is from TF2 Model Zoo
RUN eta install models

# Requires an 'images' directory be present in the project root.
# By default, this is standard behavior. Docker compose handles this
# by mapping the host machine's image-recognition/images directory
# to the container's app/images directory.

# The same is true for ./out
CMD ["conda", "run", "-n", "object-recognition", "python", "src/main.py", "-v"]