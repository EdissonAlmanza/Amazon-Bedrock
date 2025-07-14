import boto3
import json

from similarity import cosineSimilarity
client = boto3.client(service_name = "bedrock-runtime", region_name = 'us-east-1')


facts = [
        "John F. Kennedy was the 35 President of the United States",
    "The first moon landing was in 1969",
    "The capital of France is Paris",
    "Earth is the third planet from the sun.",
    "Edisson like to play videogames",
    "I'm coding in my gaming laptop because of its graphics card capability",
    "Work hard to be successful",
    "The first computer was invented in the 1940s",
    "I like to play computer games at night"
]


newFact = "Whats the secret for a fulfilling life?"


def getEmbedding(input:str):
    response = client.invoke_model(
        body = json.dumps({
            "inputText":input,
        }),
        modelId = "amazon.titan-embed-text-v1",
        accept = 'application/json',
        contentType = 'application/json'
    )
    response_body = json.loads(response.get('body').read())
    return response_body.get('embedding')

factsWithEmbeddings = []

for fact in facts:
    factsWithEmbeddings.append({
        "text":fact,
        "embedding":getEmbedding(fact)
    })


newFactEmbedding = getEmbedding(newFact)
similarities = []


for facto in factsWithEmbeddings:
    similarities.append({
        "text":facto['text'],
        "similarity": cosineSimilarity(facto['embedding'],newFactEmbedding)
    })


print(f"Similarities for fact: '{newFact}' with:")
similarities.sort(key=lambda x: x['similarity'], reverse=True)
for similarity in similarities:
    print(f"    '{similarity['text']}': {similarity['similarity']:.20f}")
