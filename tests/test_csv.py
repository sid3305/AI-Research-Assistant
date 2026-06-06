from app.utils.csv_processor import CSVProcessor


processor = CSVProcessor()

summary = processor.summarize_csv(
    "titanic.csv"
)

print(summary)