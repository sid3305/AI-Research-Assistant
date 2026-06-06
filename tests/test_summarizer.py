# test_summarizer.py

from app.services.agents.summarizer_agent import (
    SummarizerAgent
)

evidence = {
    "What is the project about?": [
        "This project predicts disease risk.",
        "The system also predicts readmission."
    ]
}

summarizer = SummarizerAgent()

context = (
    summarizer.summarize(
        evidence
    )
)

print(context)