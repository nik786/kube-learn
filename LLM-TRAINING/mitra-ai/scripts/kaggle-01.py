import os
import subprocess
import json

# Set environment variables
os.environ['KAGGLE_USERNAME'] = ''
os.environ['KAGGLE_KEY'] = ''

# Run kaggle datasets list and capture output
result = subprocess.run(
    ['kaggle', 'datasets', 'list'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Print output or errors
if result.returncode == 0:
    print(result.stdout)
else:
    print("Error:", result.stderr)

