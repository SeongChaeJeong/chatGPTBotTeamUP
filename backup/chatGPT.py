import os
import openai
import json
import argparse
from dotenv import load_dotenv

class OpenAIGpt:
    def run(self, msg):
        openai.api_key = os.getenv("OPENAI_APK_KEY")
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"{msg}.",
            temperature=0.8,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=None
        )

        return response.choices[0].text.strip()

load_dotenv()

try:
    openai_gpt = OpenAIGpt()
    # 팀업에서 메시지 가져오기
    ans = openai_gpt.run("visualstudio code 에서 python 인터프리터 설정하는 법 알려줘")
    print(ans)

    # 봇에서 팀업으로 쏘기

except Exception as e:
    print("Error createing conversation: {}".format(e))