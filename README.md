
# Come warm yourself by the hearth!

This is a project I am creating to practice.

## To run lambda unit tests
Navigate to the src folder
```
$ python -m unittest discover
```

## Create and activate the virtual environment and synthing the app

```
virtualenv venv
```
# Activaite the virtual environment
```
$ source.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements-dev.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```