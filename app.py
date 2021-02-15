from aws_cdk import core
from pipeline_lib.pipeline_master_stack import PipelineMasterStack
from pipeline_lib.pipeline_dev_stack import PipelineDevStack
from dotenv import load_dotenv
import os

load_dotenv()

app = core.App()

PipelineDevStack(
    app,
    "{}-dev-pipeline".format(app.node.try_get_context('service_name')),
    env={
        'region': "ap-northeast-1",
        'account': app.account
    }
)

PipelineMasterStack(
    app,
    "{}-master-pipeline".format(app.node.try_get_context('service_name')),
    env={
        'region': "ap-northeast-1",
        'account': app.account
    }
)

app.synth()