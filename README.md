# Object Recognizer
Object Recognizer software (CSCI 338 Final Project).
- Utilizes [FiftyOne](https://github.com/voxel51/fiftyone), an open-source computer vision wrapper, to identify common objects in scenes and label them for viewing (based on pre-trained COCO models).

## Usage
__**👮 Prerequisites**__
- [Docker](https://docs.docker.com/get-docker/) or virtual environment properly configured.
- [NVIDIA Docker Driver](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#how-do-i-install-the-nvidia-driver) (if on Linux with an NVIDIA GPU)
- (For GPU Acceleration) An NVIDIA GPU with the latest driver installed.

__**⚠️ Important Notes**__
- The source code does not run on Windows in the application's current state due to 
FiftyOne's dependency on [eta](https://pypi.org/project/voxel51-eta/). The application
functions completely through Docker for this reason, which runs a lightweight Linux environment. The source *does* run on Linux and MacOS (including M1, if `tensorflow-deps`, `tensorflow-macos` and `tensorflow-metal` are present, more details below).
- The reason code does not run on Windows is due to the `eta install models` function being Linux and MacOS specific. WSL2 is untested, however, so if a correct virtual environment were to be configured through WSL2, it is likely the application will run outside of the containerized environment.
- `./images` and `./out` are linked to the Docker container through a volume. Any images placed in the host machine's `./images` directory will be processed by the object recognizer, despite the virtualization, and will have the output placed in the host machine's `./out` directory.
- This program will execute without a GPU.
- It is **strongly** encouraged to run all below commands through WSL2 if on Windows. More info [here](https://docs.microsoft.com/en-us/windows/wsl/install).
- It is **not** recommended to run the application with different program arguments through docker as environment variables are not supported. Verbose logging is enabled by default in the Dockerfile.

### 🐋 Run with Docker
First, build the image.
```
docker build --no-cache -t object-recognizer:latest .
```

Then, run it.

__System with NVIDIA GPU__
```
docker run -it --rm --gpus all -v $(pwd)/images:/app/images -v $(pwd)/videos:/app/videos -v $(pwd)/out:/app/out object-recognizer:latest
```

__System without GPU__
```
docker run -it --rm -v $(pwd)/images:/app/images -v $(pwd)/videos:/app/videos -v $(pwd)/out:/app/out object-recognizer:latest
```

### Run from source (Linux, MacOS, and WSL2 [untested] Only)
Clone the repository
```
git clone https://github.com/theguy951357/image-recognition.git
cd image-recognition
```

Install [Miniconda3](https://docs.conda.io/en/latest/miniconda.html)

Configure the virtual environment
```
conda create -n image-recognition
conda activate image-recognition python=3.9
pip install -r requirements.txt
```

Install necessary models
```
eta install models
```

For MacOS Only:
```
conda install -c apple tensorflow-macos
pip install tensorflow-deps
```

For MacOS with ARM (M1) (in addition to the above MacOS commands):
- ```
  pip install tensorflow-metal
  ```
- Configure this environment variable (to override a "missing GPU" false-positive):
- ```
  FIFTYONE_REQUIREMENT_ERROR_LEVEL=2
  ```

Your virtual environment should now be configured with your IDE to run/debug code. In any case, run `python src/main.py` to launch the program. Feel free to use the CLI when running from source.


### CLI
- **Note:** Although CLI functionality is supported, running program arguments through Docker is **not** recommended.

This program is a console-based Python application, so a CLI is used for all program functions. The program can be executed with any of the following arguments.

```
(Help)
-h / --help - Display help prompt and all arguments.

(Optional)
-i -- Absolute or relative file path of image to process for object recognition. (Default = ./images)
-o / --out - Folder location for output. Used with -i. Default is ./out/ for image mode and ./models/ for training mode.
-v / --verbose - Verbose logging
```
**Standard Use**

Load an image into `image-recognition/images` and run the program (make sure to run from the `image-recognition` directory).

`python3 main.py -i path/to/images -o path/to/out`

**Debugging**

*Use any configuration with `-v` for verbose logging.*


### Issues
- If you get any error related to mongodb, execute the following steps.

Launch a docker instance of MongoDB
```
docker run -d mongo
```

Add the following environment variable (either in your terminal or IDE):

```
FIFTYONE_DATABASE_URI=mongodb://localhost
```