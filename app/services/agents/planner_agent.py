class PlannerAgent:

    def __init__(self):
        pass

    def plan(self,question):

        question = question.strip()

        if not question:

            return {
                "intent": "unknown",
                "tasks": []
            }

        lower_question = (
            question.lower()
        )

        intent = "retrieve"

        if "compare" in lower_question:

            intent = "compare"

        elif "summarize" in lower_question:

            intent = "summarize"

        elif "explain" in lower_question:

            intent = "explain"

        clean_question = question

        instruction_words = [
            "Compare",
            "Summarize",
            "Explain",
            "compare",
            "summarize",
            "explain"
        ]

        for word in instruction_words:

            clean_question = (
                clean_question.replace(
                    word,
                    ""
                )
            )

        clean_question = (
            clean_question.strip()
        )

        separators = [
            " and ",
            " vs ",
            " versus "
        ]

        for separator in separators:

            if separator in clean_question.lower():

                tasks = [
                    task.strip()
                    for task in clean_question.split(
                        separator
                    )
                    if task.strip()
                ]

                return {
                    "intent": intent,
                    "tasks": tasks
                }

        return {
            "intent": intent,
            "tasks": [clean_question]
        }
    