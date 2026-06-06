from app.services.prompt_builder import (
    PromptBuilder
)

from app.services.gemini_client import (
    GeminiClient
)


def main():

    context = """
Artificial Intelligence helps healthcare.

Machine learning improves diagnosis.
"""

    question = (
        "How does AI help medicine?"
    )

    prompt_builder = (
        PromptBuilder()
    )

    gemini_client = (
        GeminiClient()
    )

    prompt = (
        prompt_builder.build_prompt(
            context,
            question
        )
    )

    response = (
        gemini_client.generate_response(
            prompt
        )
    )

    print(
        "\nPrompt:\n"
    )

    print(prompt)

    print(
        "\nResponse:\n"
    )

    print(response)


if __name__ == "__main__":
    main()