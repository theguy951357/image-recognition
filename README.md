# Object Classification
Object classification software (CSCI 338 Final Project)

## Usage
### Docker
__**Prerequisites**__
- [Docker](https://docs.docker.com/get-docker/)
- [NVIDIA Docker Support](https://github.com/NVIDIA/nvidia-docker) (if using NVIDIA GPU) 

Run `docker-compose up` from this project's root directory.

### CLI
This program is a console-based Python application, so a CLI is used for all program functions. The program can be executed with any of the following arguments.

```
(Help)
-h / --help - Display help prompt and all arguments.

(Optional)
-i -- Absolute or relative file path of image to process for object recognition. (Default = ./images)
-o / --out - Folder location for output. Used with -i. Default is ./out/ for image mode and ./models/ for training mode.
-v / --verbose - Verbose logging
```

### Possible Configurations
**Standard Use**

Load an image into `image-recognition/images` and run the program (make sure to run from the `image-recognition` directory).

`python3 main.py -i path/to/images -o path/to/out`

**Debugging**

*Use any configuration with `-v` for verbose logging.*