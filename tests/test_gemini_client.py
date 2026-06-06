from app.services.gemini_client import (
    GeminiClient
)


def main():

    client = GeminiClient()

    response = (
        client.generate_response(
            "Hello Gemini. Introduce yourself in two sentences."
        )
    )

    print("\nResponse:\n")

    print(response)


if __name__ == "__main__":
    main()