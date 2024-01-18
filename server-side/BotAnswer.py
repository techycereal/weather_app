import requests
import json

# Define the endpoint and headers


def query(question, weather, temp):
    print('here')
    url = "https://weatherbotqa.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=WeatherBot&api-version=2021-10-01&deploymentName=production"
    headers = {
        "Ocp-Apim-Subscription-Key": "e0793a78635a4141b0f97b1a6cdc02ab",
        "Content-Type": "application/json"
    }

    # Define the data payload
    data = {
        "top": 3,
        "question": question,
        "includeUnstructuredSources": True,
        "confidenceScoreThreshold": 0.3,
        "filters": {
            "metadataFilter": {
                "logicalOperation": "AND",
                "metadata": [
                    {"key": "weather", "value": weather},
                    {"key": "temp", "value": temp}
                ]
            }
        }
    }
# Make the POST request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check the response
    if response.status_code == 200:
        print("Response:", response.json()['answers'][0]['answer'])
    else:
        print("Error:", response.status_code, response.text)
        
    return response.json()['answers'][0]['answer']

