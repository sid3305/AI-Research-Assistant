from app.services.agents.planner_agent import PlannerAgent
from app.services.agents.retriever_agent import RetrieverAgent
from app.services.agents.summarizer_agent import SummarizerAgent

from app.services.vector_store import vector_store
from app.utils.faiss_manager import FAISSManager
from app.services.embedding_service import EmbeddingService


chunks = [
    "This project predicts disease risk.",
    "The system predicts patient readmission.",
    "Random Forest and XGBoost are used."
]

embedding_service = EmbeddingService()

vectors = [
    embedding_service.create_embedding(chunk)
    for chunk in chunks
]

dimension = len(vectors[0])

faiss_manager = FAISSManager(dimension)

faiss_manager.add_vectors(vectors)

vector_store.set_chunks(chunks)
vector_store.set_faiss_manager(faiss_manager)


planner = PlannerAgent()
retriever = RetrieverAgent()
summarizer = SummarizerAgent()

question = "What is the project about?"

tasks = planner.plan(question)

print("\nTASKS")
print(tasks)

evidence = retriever.retrieve(tasks)

print("\nEVIDENCE")
print(evidence)

context = summarizer.summarize(evidence)

print("\nCONTEXT")
print(context)