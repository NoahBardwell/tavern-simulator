
# Come warm yourself by the hearth!

This is a project I am creating to practice.

## To run lambda unit tests
Navigate to the src folder
```
$ python -m unittest discover
```

## Activating the virtual environment and synthing the app

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```