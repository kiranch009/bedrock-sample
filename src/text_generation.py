import boto3
import json

bedrock_runtime_client = boto3.client("bedrock-runtime")


def zero_shot_generation() -> None:
    prompt_data: str = (
        """Command: Write an email from Bob, Customer Service Manager, to the customer "John Doe" who provided negative feedback on the service provided by our customer support engineer"""
    )
    body = json.dumps(
        {
            "inputText": prompt_data,
            "textGenerationConfig": {
                "maxTokenCount": 1024,
                "topP": 0.95,
                "temperature": 0.1,
            },
        }
    )

    response = bedrock_runtime_client.invoke_model(
        modelId="amazon.titan-text-express-v1",
        accept="application/json",
        contentType="application/json",
        body=body,
    )

    response_body_stream = response.get("body")

    if response_body_stream:
        response_body = json.loads(response_body_stream.read().decode("utf-8"))
        result = response_body.get("results")[0]
        print("printing results")
        print(result.get("completionReason"))
        print(result.get("outputText"))


zero_shot_generation()
