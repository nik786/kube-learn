
from datasets import load_dataset
from datasets.exceptions import DatasetNotFoundError

DATASET_CANDIDATES = [
    ("PaulAdversarial/all_news_finance_sm_1h2023", "train"),
    ("financial_phrasebank", "sentences_allagree"),
    ("reuters21578", "ModApte"),
    ("ag_news", "train"),
]

def load_news_dataset():
    for dataset_id, split in DATASET_CANDIDATES:
        try:
            print(f"Trying dataset: {dataset_id} [{split}] ...")
            dataset = load_dataset(dataset_id, split=split)
            print(f"✅ Loaded dataset: {dataset_id}")
            return dataset
        except DatasetNotFoundError:
            print(f"❌ Dataset not found: {dataset_id}")
        except Exception as e:
            print(f"⚠️ Error loading {dataset_id}: {e}")

    raise RuntimeError("❌ No valid dataset could be loaded. Check dataset IDs.")

# -------------------------
# Main execution
# -------------------------
news_dataset = load_news_dataset()

print(news_dataset)
print("Columns:", news_dataset.column_names)
print("Total records:", len(news_dataset))
