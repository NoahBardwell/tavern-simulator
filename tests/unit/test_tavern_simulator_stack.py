import aws_cdk as core
import aws_cdk.assertions as assertions

from tavern_simulator.tavern_simulator_stack import TavernSimulatorStack

def test_lambda_created():
    app = core.App()
    stack = TavernSimulatorStack(app, "tavern-simulator")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties(
        "AWS::Lambda::Function",
        {
            "Handler": "handler",
            "Runtime": "nodejs14.x",
        },
    )
