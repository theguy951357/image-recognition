# Object Classification
Object classification software (CSCI 338 Final Project)


## CLI
This program is a console-based Python application, so a CLI is used for all program functions. The program can be executed with any of the following arguments.

```
(Help)
-h / --help - Display help prompt and all arguments.

(Required for standard use of the program.)
-i / --image - Absolute or relative file path of image to process for object recognition.

(Optional / Debug)
-m / --model - File location of the model to use for object classification. If omitted, will use ./models/default.pb -- Application will not run if this file or directory is missing. Used with -i.
-n / --name - Name of the output image file. Default is output-# where # is the number of output files already present in the directory for image mode. Default output for model mode if model-#. Used with -o and -i. Do not specify a file-type at the end of the name as it will be ignored.
-o / --out - Folder location for output. Used with -i. Default is ./out/ for classification mode and ./models/ for training mode.

(Training)
-t / --train - Path to image folder to train the model from. This also sets the application into a training configuration.
-e / --epochs - Number of Tensorflow epochs to use in the training. Default is 10.

(Debugging)
-v / --verbose - Verbose logging
```

### Possible Configurations
**Standard Use**

`python3 main.py -i path/to/image -o path/to/out`

`python3 main.py -i path/to/image -o path/to/out -m ./models/my-model.pb -n my-name`

**Model Training**

`python3 main.py -t image/dir`

`python3 main.py -t another/image/dir -o my/model/dir -e 20 -n my-model`

**Debugging**

*Use any standard configuration with `-v` for verbose logging.*

Note: Incompatible arguments will cause the application not to run. For example, the following would **NOT** work as the application would be trying to train and produce a result at the same time, which is incompatible behavior.

`python3 main.py -i path/to/image -o path/to/out -t my/image/dir -e 15`.

### Exhaustive Configuration Compatibilities
/ | -i | -m | -n | -o | -t | -e | -v
---|---|---|---|---|---|---|---|
-i|✔️|✅|✅|✅|❌|❌|✅
-m|✅|✔️|✅|✅|❌|❌|✅
-n|✅|✅|✔️|✅|✅|✅|✅
-o|✅|✅|✅|✔️|✅|✅|✅
-t|❌|❌|✅|✅|✔️|✅|✅
-e|❌|❌|✅|✅|✅|✔️|✅
-v|✅|✅|✅|✅|✅|✅|✔️


