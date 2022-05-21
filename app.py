#!/usr/bin/env python3
import aws_cdk as cdk

from tavern_simulator.tavern_simulator_stack import TavernSimulatorStack


app = cdk.App()
TavernSimulatorStack(app, "TavernSimulatorStack")

app.synth()
