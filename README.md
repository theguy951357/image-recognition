# Object Classification
Object classification software (CSCI 338 Final Project)

## Configure Installation
### Windows
Install [miniconda](https://docs.conda.io/en/latest/miniconda.html) (there are .exe download links there). Make sure to select the option that allows for IDEs to auto-detect the conda install. It should warn you in red letters if you try to un-check it.

Install all prerequisites shown [here](https://www.tensorflow.org/install/gpu) under the "Software Requirements" section (drivers, CUDA, etc.). You will need to create an account for the Nvidia CUDA download. Leave this tab open, you'll need it again later.

After all software from the Tensorflow GPU page is installed, download the `cudnn64_8.dll` from [here](https://www.dll-files.com/download/dae6bbb218bc4091223a48a97b6eba4b/cudnn64_8.dll.html?c=UWVyZGMrUEdoamJVRWhiQlNKaXJsZz09) and move it into your `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.6\bin` folder (replace `11.6` with your version if it differs).

Revisit the Tensorflow GPU tab and follow the instructions at the bottom for configuring your PATH. Execute the commands in a standard Windows command prompt, not PowerShell.

**Reboot**

Now, Open the Anaconda (Miniconda3) prompt (available via Windows search).

Execute the following to configure the new environment. Run from the root directory of this project.

`conda create -n object-recognition python=3.9`

`conda activate object-recognition`

`pip install -r requirements.txt`

You are now able to setup PyCharm to run through Miniconda (default directory is `C:\Users\<you>\miniconda3`)


## Usage
### CLI
This program is a console-based Python application, so a CLI is used for all program functions. The program can be executed with any of the following arguments.

**NOTE:** `-i` and `-t` are **incompatible.** Read below for further details.
```
(Help)
-h / --help - Display help prompt and all arguments.

(Required for image mode.)
-i / --image - Absolute or relative file path of image to process for object recognition.

(Required for training mode. -i and -t are incompatible.)
-t / --train - Path to image folder to train the model from. This also sets the application into a training configuration.

(Optional / Debug)
-m / --model - File location of the model to use for object classification. If omitted, will use ./models/default.pb -- Application will not run if this file or directory is missing.
-n / --name - Name of the output image file. Default is output-# where # is the number of output files already present in the directory for image mode. Default output for model mode if model-#. Do not specify a file-type at the end of the name as it will be ignored.
-o / --out - Folder location for output. Used with -i. Default is ./out/ for image mode and ./models/ for training mode.
-e / --epochs - Number of Tensorflow epochs to use in the training. Default is 10.
-v / --verbose - Verbose logging
```

### Possible Configurations
**Standard Use**

Use `-i` to activate image mode. Point to an image's file path to import it into the program. A specific model path may be specified for which to classify the objects in the image from.

`python3 main.py -i path/to/image -o path/to/out`

`python3 main.py -i path/to/image -o path/to/out -m ./models/my-model.pb -n my-name`

**Model Training**

Use `-t` to activate model training mode. Point to a directory for training data.

`python3 main.py -t image/dir`

`python3 main.py -t another/image/dir -o my/model/dir -e 20 -n my-model`

**Debugging**

*Use any configuration with `-v` for verbose logging.*

Note: Incompatible arguments will cause the application not to run. For example, the following would **NOT** work as the application would be trying to train and produce a result at the same time, which is incompatible behavior.

`python3 main.py -i path/to/image -o path/to/out -t my/image/dir -e 15`.
