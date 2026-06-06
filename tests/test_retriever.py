# test_retriever.py

from app.services.agents.planner_agent import (
    PlannerAgent
)

from app.services.agents.retriever_agent import (
    RetrieverAgent
)

planner = PlannerAgent()


retriever = RetrieverAgent()

tasks = planner.plan(
    "What is the project about?"
)

evidence = (
    retriever.retrieve(tasks)
)

print(evidence)