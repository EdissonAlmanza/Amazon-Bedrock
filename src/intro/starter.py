# Imports Boto3 whichs is AWS SDK for python - Provides python API for AWS infrastructure services
import boto3
import pprint # Pretty print


# Create a low-level service client by name using the default session.
# service name: the name of a service. eg. s3, ec2, bedrock, etc. 
# region_name: the name of the region associated with the client

bedrock = boto3.client(
    service_name = 'bedrock',
    region_name = 'us-east-1')

pp = pprint.PrettyPrinter(depth=4) 


def list_foundation_models():
    # Get a list of the available models (json)
    models = bedrock.list_foundation_models()
    for model in models['modelSummaries']:
        pp.pprint(model)
        pp.pprint("--------------------------")


def get_foundation_model(modelIdentifier):
    model = bedrock.get_foundation_model(modelIdentifier = modelIdentifier)
    pp.pprint(model)

list_foundation_models()