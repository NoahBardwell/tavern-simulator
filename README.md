
# Come warm yourself by the hearth!

This is a project I am creating to work on building the ideal aws template.

Auth Cognito -> ApiGateway (Payload) -> AWS Lambda

## Install awscli
```
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
```

## Create and activate the virtual environment and synthing the app

```
virtualenv venv

```
## Activate the virtual environment with
```
$ source.bat
```
or 
```
$ source venv/bin/activate
```

Once the virtualenv is activated, install the required dependencies.
```
$ pip install -r requirements-dev.txt
```

Synthesize the CloudFormation template for this code.
```
$ cdk synth
```

## Tests

### Run tests
Navigate to top project directory
```
$ coverage run -m unittest discover
```

### Test coverage report
```
$ coverage report
```