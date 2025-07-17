import boto3
import json

AWS_REGION_BEDROCK = 'us-east-1'

client = boto3.client(service_name = 'bedrock-runtime',
                      region_name = AWS_REGION_BEDROCK)


def handler(event, context):
    """
    AWS Lambda function to summarize a text using the Amazon Titan model.

    Expects an HTTP request event with a JSON body containing 'text', and a 
    'points' parameter in the query string. It calls the Titan model for 
    summarization and returns the result as a JSON response.

    Args:
        event (dict): AWS Lambda event object containing request data. 
            - event["body"]: JSON string with 'text' key.
            - event["queryStringParameters"]["points"]: Number of summary points.
        context: AWS Lambda context object (unused).

    Returns:
        dict: API Gateway-compatible response object containing either the summary 
        result or an error message.

    Example:
        # API Gateway event with text in body and points in query string
        >>> handler(
        ...     {"body": '{"text": "Once upon a time..."}', "queryStringParameters": {"points": "3"}},
        ...     None
        ... )
        {
            "statusCode": 200,
            "body": '{"summary": "..."}'
        }
    """
    body = json.loads(event["body"])
    text = body.get("text")
    points = event["queryStringParameters"]["points"]

    if text and points:
        titan_config = get_titan_config(text, points)
        response = client.invoke_model(
            body = titan_config,
            modelId = "amazon.titan-text-express-v1",
            accept = "application/json",
            contentType = "application/json"
        )
        response_body = json.loads(response.get("body").read())
        result = response_body.get("results")[0]
        return{
            "statusCode":200,
            "body": json.dumps({"summary": result.get("outputText")}),
        }
    return {
        "statusCode": 400,
        "body": json.dumps({"error": "text and points required!"}),
    }

def get_titan_config(text: str, points: str):
    
    """
    Generate a JSON configuration string for text summarization using the Titan model.

    Constructs a prompt instructing the model to summarize the given text in a specified 
    number of points, and returns a JSON-formatted string with the prompt and generation 
    configuration parameters.

    Args:
        text (str): The input text to be summarized.
        points (str): The number of summary points to generate.

    Returns:
        str: A JSON string containing the prompt and text generation configuration.

    Example:
        >>> get_titan_config("Once upon a time...", "3")
        '{"inputText": "...", "textGenerationConfig": {...}}'
    """

    prompt = f"""Text: {text} \n
        From the text above, summarize the story in {points} points. \n """
    
    return json.dumps(
        {
            "inputText" : prompt,
            "textGenerationConfig": {
                "maxTokenCount": 4096,
                "stopSequences": [],
                "temperature": 0,
                "topP": 1,
            },
        }
    )