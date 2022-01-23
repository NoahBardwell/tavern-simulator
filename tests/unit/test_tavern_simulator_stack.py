import aws_cdk as core
import aws_cdk.assertions as assertions

from tavern_simulator.tavern_simulator_stack import TavernSimulatorStack

# example tests. To run these tests, uncomment this file along with the example
# resource in tavern_simulator/tavern_simulator_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TavernSimulatorStack(app, "tavern-simulator")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
