import os
import logging
import openai
import json
import argparse
import requests
from fake_useragent import UserAgent
import ssl
from dotenv import load_dotenv

ssl._create_default_https_context = ssl._create_unverified_context

logger = logging.getLogger("teamup-bot")
user_agent = UserAgent()

class OpenAIGpt:
    def run(self, user_chat_contents):

        url = "https://api.openai.com/v1/chat/completions"

        api_key = os.getenv("OPENAI_APK_KEY")
        # Prompt
        # Request headers
        headers = {
            'User-Agent': user_agent.random,
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        to_messages=[]
        for gpt_item in user_chat_contents:
            logger.debug("role={value1}, content={value2}".format(value1=gpt_item.role, value2=gpt_item.content))
            to_messages.append({"role" : gpt_item.role, "content" : gpt_item.content})

        # Request data
        data = {
            "model": "gpt-3.5-turbo",
            "messages": to_messages
            #"messages": [{"role": "user", "content": prompt }]
        }

        logger.debug(data)
        # Send the API request
        response = requests.post(url, headers=headers, verify=False, data=json.dumps(data))

        # Get the generated text from the response
        generated_text = response.json()["choices"][0]["message"]["content"]
        return generated_text.strip()

load_dotenv()
