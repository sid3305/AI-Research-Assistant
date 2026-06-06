import os

from dotenv import load_dotenv

import google.generativeai as genai


class GeminiClient:

    def __init__(self):

        load_dotenv()

        api_key = os.getenv(
            "GEMINI_API_KEY"
        )

        if not api_key:

            raise ValueError(
                "GEMINI_API_KEY not found"
            )

        genai.configure(
            api_key=api_key
        )

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def generate_response(
        self,
        prompt
    ):

        response = self.model.generate_content(
            prompt
        )

        return response.text