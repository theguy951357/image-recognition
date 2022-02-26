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

(Required for image mode.)
image_dir -- Absolute or relative file path of image to process for object recognition. (Default = ./images)

(Optional)
-o / --out - Folder location for output. Used with -i. Default is ./out/ for image mode and ./models/ for training mode.
-v / --verbose - Verbose logging
```

### Possible Configurations
**Standard Use**

Use `-i` to activate image mode. Point to an image's file path to import it into the program. A specific model path may be specified for which to classify the objects in the image from.

`python3 main.py -i path/to/image -o path/to/out`

**Debugging**

*Use any configuration with `-v` for verbose logging.*