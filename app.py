#!/usr/bin/env python3
import os

import aws_cdk.core as cdk

from tavern_simulator.tavern_simulator_stack import TavernSimulatorStack


app = cdk.App()
TavernSimulatorStack(app, "TavernSimulatorStack")

app.synth()
