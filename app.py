#!/usr/bin/env python3

from aws_cdk import core

from the_system.the_system_stack import TheSystemStack


app = core.App()
TheSystemStack(app, "the-system")

app.synth()
