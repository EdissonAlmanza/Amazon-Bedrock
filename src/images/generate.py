import boto3
import json
import base64

client = boto3.client(service_name = 'bedrock-runtime', region_name = 'us-east-1')

titan_image_config =json.dumps({
    "taskType": "TEXT_IMAGE",
    "textToImageParams": {
        "text": "videogame character that is an AI engineer",
    },
    "imageGenerationConfig": {
        "numberOfImages": 1,
        "height": 512,
        "width": 512,
        "cfgScale": 8  #specify how strongly the generated image should adhere to the prompt. Lower value indicate more randomness. 
    }
})


response = client.invoke_model(
    body = titan_image_config,
    modelId = 'amazon.titan-image-generator-v1',
    accept = 'application/json',
    contentType = 'application/json'
)

response_body = json.loads(response.get("body").read())
base64_image = response_body.get("images")[0]

base_64_image = base64.b64decode(base64_image)


file_path = "engineer.png"

with open(file_path, "wb") as f:
    f.write(base_64_image)