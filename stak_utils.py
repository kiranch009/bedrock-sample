from constructs import Construct


def getEnv(stack: Construct, key: str) -> str:
    """
    Get the environment name from the stack's environment.
    """

    return stack.node.try_get_context("env").get(key) or stack.node.try_get_context(
        "env"
    ).get("default")


def getStage(stack: Construct) -> str:
    """
    Get the stage name from the stack's environment.
    """
    return stack.node.try_get_context("stage")
