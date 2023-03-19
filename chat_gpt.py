import os
import openai
import json
import argparse
import requests
from dotenv import load_dotenv

class OpenAIGpt:
    def run(self, msg):

        url = "https://api.openai.com/v1/chat/completions"

        api_key = os.getenv("OPENAI_APK_KEY")
        # Prompt
        prompt = f"{msg}"
        # Request headers
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        # Request data
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt }]
        }
        # Request data
        #data = {
        #    "prompt": prompt,
        #    "max_tokens": 1024,
        #    "n": 1,
            #"stop": "\n"
        #}

        # Send the API request
        response = requests.post(url, headers=headers, data=json.dumps(data))

        # Get the generated text from the response
        generated_text = response.json()["choices"][0]["message"]["content"]
        return generated_text.strip()

        #openai.api_key = os.getenv("OPENAI_APK_KEY")
        #response = openai.Completion.create(
        #    model="text-davinci-003",
        #    prompt=f"{msg}.",
        #    temperature=1,
        #    max_tokens=1024,
        #    top_p=1,
        #    frequency_penalty=0.0,
        #    presence_penalty=0.0,
        #    stop=None
        #)

        #return response.choices[0].text.strip()
        

load_dotenv()

#try:
#    openai_gpt = OpenAIGpt()
    # 팀업에서 메시지 가져오기
#    ans = openai_gpt.run("visualstudio code 에서 python 인터프리터 설정하는 법 알려줘")
#    print(ans)

    # 봇에서 팀업으로 쏘기

#except Exception as e:
#    print("Error createing conversation: {}".format(e))