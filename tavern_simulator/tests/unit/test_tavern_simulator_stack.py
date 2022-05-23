import unittest
import aws_cdk as core
import aws_cdk.assertions as assertions

from tavern_simulator_stack import TavernSimulatorStack


class TavernStackTest(unittest.TestCase):

    def test_lambda_created(self):
        app = core.App()
        stack = TavernSimulatorStack(app, "tavern-simulator")
        template = assertions.Template.from_stack(stack)

        template.has_resource_properties(
            "AWS::Lambda::Function",
            {
                "Handler": "app.handler",
                "Runtime": "python3.9",
            },
        )
