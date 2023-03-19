import requests
import json

# API endpoint URL
url = "https://api.openai.com/v1/engines/davinci-codex/completions"

# API key
api_key = "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"

# Prompt
prompt = "구로구에 추천해줄 만한 도서관은 어디야?"

# Request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Request data
data = {
    "prompt": prompt,
    "max_tokens": 50,
    "n": 1,
    "stop": "\n"
}

# Send the API request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Get the generated text from the response
generated_text = response.json()["choices"][0]["text"]

# Print the generated text
print(generated_text)
