from multiprocessing import context

from app.services.prompt_builder import (PromptBuilder)

from app.services.gemini_client import (GeminiClient)

from app.services.agents.planner_agent import (PlannerAgent)

from app.services.agents.retriever_agent import (RetrieverAgent)

from app.services.agents.summarizer_agent import (SummarizerAgent)


class RAGService:

    def __init__(self):

        self.prompt_builder = (PromptBuilder())

        self.gemini_client = (GeminiClient())

        self.planner_agent = (PlannerAgent())

        self.retriever_agent = (RetrieverAgent())

        self.summarizer_agent = (SummarizerAgent())
        
    
    def answer_question(self, question):

        plan = (self.planner_agent.plan(question))
        tasks = plan["tasks"]
        evidence = (
            self.retriever_agent.retrieve(
                tasks
            )
        )

        context = (
            self.summarizer_agent.summarize(
                evidence,
                plan["intent"]
            )
        )

        prompt = (
            self.prompt_builder.build_prompt(
                context,
                question
            )
        )

        answer = (
            self.gemini_client.generate_response(
                prompt
            )
        )

        return {
            "question": question,
            "context": context,
            "answer": answer
        }