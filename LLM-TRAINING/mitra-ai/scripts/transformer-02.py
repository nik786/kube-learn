import os
import warnings
import torch
from transformers import pipeline

# Suppress logs
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
warnings.filterwarnings("ignore")

# Force CPU usage
torch.cuda.is_available = lambda: False
torch.set_num_threads(4)

# Load pipeline
roberta = pipeline(
    "zero-shot-classification",
    model="typeform/distilbert-base-uncased-mnli",
    device=-1
)

def pretty_print(result):
    """Print results in a formatted table."""
    print("\n📄 Sequence:")
    print(result['sequence'])
    print("\n🔍 Classification Results:")
    print(f"{'Label':<25}Score")
    print("-" * 35)
    for label, score in zip(result['labels'], result['scores']):
        print(f"{label:<25}{score:.4f}")
    best_label = result['labels'][result['scores'].index(max(result['scores']))]
    print("\n🏆 Best Match:", best_label)
    print("=" * 50)

# 1️⃣ First example
sequence1 = """Subject: Action Plan & Next Steps for Project Alpha
Hi Team,
Following up on our discussion, I've outlined a clear action plan to boost our team's productivity and ensure we meet our upcoming deadlines for Project Alpha.
Here are the key tasks and their owners:
Task 1: Finalize Q3 Report - Assigned to: [Name] - Deadline: End of Day, Friday.
Task 2: Develop a new marketing strategy - Assigned to: [Name] - Deadline: Wednesday, next week.
Task 3: Schedule a follow-up meeting to track our progress.
I've also shared a document with some time management and workflow optimization tips that I believe will be beneficial. Please review it and come prepared to our next meeting to discuss how we can implement these strategies.
Our goal is to enhance our overall efficiency and achieve our targets. Let's work together to make this a success.
Best,
[Your Name]"""
labels1 = ['task', 'event', 'tutorial', 'work']
pretty_print(roberta(sequence1, labels1))

# 2️⃣ Second example
sequence2 = "Our organization's next quarter sales is likely to drop"
labels2 = ['company information', 'public information']
pretty_print(roberta(sequence2, labels2))

# 3️⃣ Third example
sequence3 = "How do I make biriyani well?"
labels3 = ['billing', 'account creation', 'product issues', 'other']
pretty_print(roberta(sequence3, labels3))

# 4️⃣ Fourth example
sequence4 = "Virat Kohli is an awesome player."
labels4 = ['cricket', 'football', 'tennis', 'medicine']
pretty_print(roberta(sequence4, labels4))

