from aws_cdk import Stack, aws_s3 as s3
from constructs import Construct


class ChatbotStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        stage = self.node.try_get_context("stage")

        s3.Bucket(
            self,
            f"{stage}-kc-bedrock-knowledge-base-source-id",
            bucket_name=f"{stage}-kc-bedrock-knowledge-base-source",
        )
