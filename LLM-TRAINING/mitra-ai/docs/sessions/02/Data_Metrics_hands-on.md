

```

# Create y array (ground truth)
y     = np.array([1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1])

# Create y_hat array (predicted values)
y_hat = np.array([1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0])
len(y)

```

```
y == y_hat

(y == y_hat).sum()

accuracy = 10 / len(y)
accuracy

```

```

def calculate_true_positives_negatives(y_true, y_pred):
    true_positives = np.sum((y_true == 1) & (y_pred == 1))
    true_negatives = np.sum((y_true == 0) & (y_pred == 0))
    return true_positives, true_negatives

# Call the function with the given arrays
tp, tn = calculate_true_positives_negatives(y, y_hat)

print("True Positives:", tp)
print("True Negatives:", tn)

```

```

# Calculate false positives and false negatives
fp = np.sum((y == 0) & (y_hat == 1))
fn = np.sum((y == 1) & (y_hat == 0))

print("False Positives:", fp)
print("False Negatives:", fn)

```

```
def calculate_sensitivity_specificity(tp, tn, fp, fn):
    sensitivity = tp / (tp + fn)
    specificity = tn / (tn + fp)
    return sensitivity, specificity

```

```
# Call the function with the given values
sensitivity, specificity = calculate_sensitivity_specificity(tp, tn, fp, fn)

print("Sensitivity:", sensitivity.round(2))
print("Specificity:", specificity.round(3))

```


zero-shot/few-shot/chain-of-thought/role-prompting/output-formatting


























