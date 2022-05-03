
# Come warm yourself by the hearth!

This is a project I am creating to practice using cdk version 2 and creating a project structure that enables easy development with aws.

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
$ source venv/bin/activate
```

Once the virtualenv is activated, you can install the required dependencies.
```
$ pip install -r requirements-dev.txt
```

At this point you can now synthesize the CloudFormation template for this code.
```
$ cdk synth
```

## To cdk stack infrastructure tests
Navigate to the src folder
```
$ python -m unittest
```

## To run lambda unit tests
Navigate to the src folder
```
$ python -m unittest
```