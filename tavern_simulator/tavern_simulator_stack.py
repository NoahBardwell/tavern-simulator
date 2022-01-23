from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
)
from constructs import Construct

class TavernSimulatorStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        tavern_lambda = _lambda.Function(
            self, 'tavern',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('src/tavern'),
            handler='app.handler',
        )
