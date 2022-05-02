
# Come warm yourself by the hearth!

This is a project I am creating to practice.

## To run lambda unit tests
Navigate to the src folder
```
$ python -m unittest discover
```
# Install awscli
```
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
```

## Create and activate the virtual environment and synthing the app

```
virtualenv venv
```
# Activate the virtual environment with
```
$ source.bat
```
or 
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