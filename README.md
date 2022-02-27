# Object Recognizer
Object Recognizer software (CSCI 338 Final Project).
- Utilizes [FiftyOne](https://github.com/voxel51/fiftyone), an open-source computer vision wrapper, to identify common objects in scenes and label them for viewing (based on pre-trained COCO models).

## Usage
__**👮 Prerequisites**__
- [Docker](https://docs.docker.com/get-docker/)
- [NVIDIA Docker Driver](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#how-do-i-install-the-nvidia-driver) (if on Linux)
- An NVIDIA GPU with the latest driver installed.

__**⚠️ Important Notes**__
- The source code does not run on Windows in the application's current state due to 
FiftyOne's dependency on [eta](https://pypi.org/project/voxel51-eta/). The application
functions completely through Docker for this reason, which runs a lightweight Linux environment. The source *does* run on Linux and MacOS (including M1, if `tensorflow-deps`, `tensorflow-macos` and `tensorflow-metal` are present).
- The reason code does not run on Windows is due to the `eta install models` function being Linux and MacOS specific. WSL2 is untested, however, so if a correct virtual environment were to be configured through WSL2, it is likely the application will run outside of the containerized environment.
- `./images` and `./out` are linked to the Docker container through a volume. Any images placed in the host machine's `./images` directory will be processed by the object recognizer, despite the virtualization, and will have the output placed in the host machine's `./out` directory.
- Output without GPU support is untested. If you do not see your GPU in the device list (it will be in the application logs), you may get bad output.
- It is **strongly** encouraged to run all below commands through WSL2 if on Windows. More info [here](https://docs.microsoft.com/en-us/windows/wsl/install).
- It is **not** recommended to run the application with different program arguments through docker as environment variables are not supported. Verbose logging is enabled by default in the Dockerfile.

### 🐋 Run with Docker
First, build the image.
```
docker build --no-cache -t object-recognizer:latest .
```

Then, run it.
```
docker run -it --rm --gpus all -v $(pwd)/images:/app/images -v $(pwd)/out:/app/out object-recognizer:latest
```

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