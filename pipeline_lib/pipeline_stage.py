# pipeline_lib/pipeline_stage.py

from aws_cdk import (
    core
)
from hello_app.hello_app_stack import HelloAppStack

class PipelineStage(core.Stage):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        HelloAppStack(self, self.node.try_get_context('service_name') + '-stack')