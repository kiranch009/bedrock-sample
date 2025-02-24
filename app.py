#!/usr/bin/env python3
import os
import aws_cdk as cdk
from stack import ChatbotStack


app = cdk.App()
stage = app.node.try_get_context("stage")
config = app.node.try_get_context("config")
vals = {**config.get("default", {}), **config.get(stage, {})}

tags = {
    "stage": stage,
}

ChatbotStack(
    app,
    f"{stage}-chatbot-stack",
    env=cdk.Environment(
        account=vals.get("account"),
        region=vals.get("region"),
    ),
    tags=tags,
)

app.synth()
