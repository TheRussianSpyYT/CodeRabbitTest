import urllib.request
import json
import os

def get_ai_response(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    api_key = os.environ.get("OPENAI_API_KEY")  # Read from environment variable

    if not api_key:
        return "Error: OPENAI_API_KEY environment variable not set"

    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
    }

    auth_header = "Bearer " + api_key

    req = urllib.request.Request(url)
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", auth_header)

    try:
        response = urllib.request.urlopen(req, data=json.dumps(data).encode('utf-8'))
        result = json.loads(response.read().decode('utf-8'))
        return result['choices'][0]['message']['content']
    except Exception as e:
        return "Error: " + str(e)

# Example usage
print(get_ai_response("Say hello in one word."))
