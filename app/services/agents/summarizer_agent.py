class SummarizerAgent:

    def __init__(self):
        pass

    def summarize(
        self,
        evidence,
        intent
    ):

        sections = []

        header = ""

        if intent == "compare":

            header = (
                "COMPARISON TASK\n\n"
            )

        elif intent == "summarize":

            header = (
                "SUMMARY TASK\n\n"
            )

        elif intent == "explain":

            header = (
                "EXPLANATION TASK\n\n"
            )

        else:

            header = (
                "RETRIEVAL TASK\n\n"
            )

        for task, chunks in evidence.items():

            section = (
                f"Topic: {task}\n\n"
            )

            if chunks:

                chunk_text = (
                    "\n\n".join(chunks)
                )

                section += (
                    f"Evidence:\n{chunk_text}"
                )

            else:

                section += (
                    "Evidence: No relevant information found."
                )

            sections.append(section)

        body = (
            "\n\n"
            + "=" * 50
            + "\n\n"
        ).join(sections)

        return header + body