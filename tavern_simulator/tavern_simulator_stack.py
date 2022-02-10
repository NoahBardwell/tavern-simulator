import aws_cdk.core as cdk
from aws_cdk.core import Stack
from constructs import Construct
import aws_cdk.aws_apigateway as _apigateway
import aws_cdk.aws_cognito as _cognito
import aws_cdk.aws_lambda as _lambda
import aws_cdk.aws_logs as _logs

class TavernSimulatorStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        tavern_lambda = _lambda.Function(
            self,
            id="Tavern",
            function_name='tavern',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('src/tavern'),
            handler='app.handler',
        )

        user_pool = _cognito.UserPool(
            self,
            id="TavernUserPool",
            user_pool_name="tavern-user-pool",
            removal_policy=cdk.RemovalPolicy.DESTROY
        )

        user_pool.add_client(
            id="TavernClient",
            user_pool_client_name="tavern-client",
            generate_secret=True,
        )

        user_pool.add_domain(
            id="TavernDomain",
            cognito_domain=_cognito.CognitoDomainOptions(
                domain_prefix="tavern-simulator"
            )
        )

        auth = _apigateway.CognitoUserPoolsAuthorizer(
            self,
            id="TavernAuthorizer",
            authorizer_name="tavern-authorizer",
            cognito_user_pools=[user_pool]
        )

        tavern_api_access_logs = _logs.LogGroup(
            self,
            id="TavernApiAccessLogs",
            removal_policy=cdk.RemovalPolicy.DESTROY,
            log_group_name="tavern-api-access-logs",
            retention=_logs.RetentionDays.ONE_MONTH
        )
        
        tavern_api = _apigateway.LambdaRestApi(
            self,
            id="TavernApi",
            handler=tavern_lambda,
            rest_api_name="taven-api",
            deploy=True,
            deploy_options=_apigateway.StageOptions(
                access_log_destination=_apigateway.LogGroupLogDestination(tavern_api_access_logs)
            )
        )
        items = tavern_api.root.add_resource("tavern-items")
        item = items.add_resource("{items}")
        item.add_method(
            http_method="GET",
            authorizer=auth,
            authorization_type=_apigateway.AuthorizationType.COGNITO
        )