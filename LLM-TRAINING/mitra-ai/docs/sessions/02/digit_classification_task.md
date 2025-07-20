

| Topic | Description |
|-------|-------------|
| Dataset | A large corpus of handwritten digit images and their corresponding labels. |
| Goal | Build an AI model that automatically learns patterns and features to correctly label future handwritten images. |
| Dataset Source | **MNIST Database** – Contains 60,000 training images and 10,000 test images of handwritten digits. |
| Tools Used | **Keras** Python API with **TensorFlow** as the backend. |
| Why Keras? | Keras is beginner-friendly, simple, and efficient for building machine learning models. Its simplicity helps turn ML ideas into reality quickly. |
| Benefits of Keras | Quick to learn, easy to use, and allows users to stack neural network layers like experts. |



## Importing the Necessary Python Modules

```
import numpy as np                   # Optimized scientific computing library
import matplotlib.pyplot as plt      # For plotting
import random                        # for generating random numbers
from keras import models             # used for loading the saved model

from keras.datasets import mnist     # importing the dataset
from keras.models import Sequential  # Model type to be used

from keras.layers import Dense, Dropout, Activation # Types of layers to be used in our model
from keras import utils as np_utils                         # NumPy related tools


```

## Loading Training Data

```

# The MNIST data is split between 60,000 28 x 28 pixel training images and 10,000 28 x 28 pixel images
train_data, test_data = mnist.load_data()
X_train, y_train = train_data
X_test, y_test = test_data

print("Printing the shapes for validation. Format for shape : (n_elements, n_rows, n_cols)")
print(f"X_train :  {X_train.shape}, y_train :  {y_train.shape}")
print(f"X_test  :  {X_test.shape}, y_test  :  {y_test.shape}")

```

https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz



Let us plot some sample images from the training set, using Matplotlib.


```
plt.rcParams['figure.figsize'] = (9,9) # Changing these values to Make the figures a bit bigger
("rc" params are like configuration parameters)

#Plotting some 9 samples in a 3x3 grid for data visualization
for i in range(9):
    plt.subplot(3,3,i+1)
    index = random.randint(0, len(X_train)) # random image index in the valid range
    plt.imshow(X_train[index], cmap='gray')  # color map -> gray as it is a black and white image
    plt.title(f"Class Label: {y_train[index]}")

plt.tight_layout()


```

Let's examine a single digit a little closer, and print out the array representing the digit.


```

np.set_printoptions(linewidth=120)  # Making line width large so that the entire first row is printed as one row!

print(np.matrix(X_train[index]))    # Let us examine the pixel values of the last number from above

```


| Comment | Description |
|---------|-------------|
| Array Input | This array is what your computer receives and operates with. |
| Pixel Pattern | If we follow the non-zero pixels we can see the number! |
| Image Type | This is a black and white image. Here the pixel values correspond to light * intensities. Each pixel is an 8-bit integer from 0-255. 0 is full black, while 255 is full white. |
| Monochrome | This is what we call a single-channel pixel. It's called monochrome. |
| Fun Fact | Your computer screen has three channels for each pixel: red, green, blue. Each of these channels also takes an 8-bit integer. 3 channels -- 24 bits total -- 16,777,216 possible colors! |


| Topic | Description |
|-------|-------------|
| Input Shape | Instead of a 28 x 28 matrix, we build our network to accept a 784-length vector. |
| Reshaping | Each image needs to be reshaped (or flattened) into a vector. |
| Normalization | Inputs are normalized to the range [0-1] rather than [0-255]. This ensures all features are on a similar scale, which is generally recommended. |
| Note on Flattening | By flattening the matrix, we lose the connectivity information of the input pixels. For example, the model doesn't know that pixels at (1,1) and (2,1) are adjacent. The model ignores spatial relationships like horizontal, vertical, or diagonal connectivity. |
| Future Insight | This limitation will be addressed later when we use Convolutional Neural Networks (CNNs), which are designed to leverage spatial information in images. |



```

X_train = X_train.reshape(60000, 784) # reshape 60,000 28 x 28 matrices into 60,000 784-length vectors.
X_test = X_test.reshape(10000, 784)   # reshape 10,000 28 x 28 matrices into 10,000 784-length vectors.

X_train = X_train.astype('float32')   # change integers to 32-bit floating point numbers
X_test = X_test.astype('float32')

X_train /= 255                        # normalize each value for each pixel for the entire vector for each input
X_test /= 255

print(f"Training matrix shape now:  {X_train.shape}")
print(f"Testing matrix shape now: {X_test.shape}")

```
```

# Converting the given y-labels to ONE HOT ENCODED VECTORS form
n_classes = 10 # number of unique digits/classes

Y_train = np_utils.to_categorical(y_train, n_classes)
Y_test = np_utils.to_categorical(y_test, n_classes)

```

model = Sequential()


# The first hidden layer is a set of 512 nodes (artificial neurons).
# Each node will receive an element from each input vector and apply some weight and bias to it.

model.add(Dense(512, input_shape=(784,))) #(784,) is not a typo -- that represents a 784 length vector!




# An "activation" is a non-linear function applied to the output of the layer above.
# It checks the new value of the node, and decides whether that artifical neuron has fired.
# The Rectified Linear Unit (ReLU) converts all negative inputs to nodes in the next layer to be zero.
# Those inputs are then not considered to be fired.
# Positive values of a node are unchanged.

model.add(Activation('relu'))
# It is this RELU FUNCTION that brings in non-linearity to the network, which then unlocks the model to be able to generalize to literally any function,
# given a large enough network!


# Dropout zeroes a selection of random outputs (i.e., disables their activation)
# Dropout helps protect the model from memorizing or "overfitting" the training data.
model.add(Dropout(0.2))


## Intuition:

If some of the nodes are randomly not available to the model for making its prediction 
during training phase, it means that the other nodes are forced to be able to make 
the right prediction, even in the absence of the missing nodes' information. 
This means, the information is forced to be uniformly spread across all the nodes of the network, and the neural network cannot cheat by using the information 
contained in one or two nodes alone for making the predictions.



# The second hidden layer appears identical to our first layer.
# However, instead of each of the 512-node receiving 784-inputs from the input image data,
# they receive 512 inputs from the output of the first 512-node layer.

model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.2))



## The Final Output Layer


# The final layer of 10 neurons in fully-connected to the previous 512-node layer.
# The final layer of a FCN should be equal to the number of desired classes (10 in this case).
model.add(Dense(10))


# The "softmax" activation represents a probability distribution over K different possible outcomes.
# Its values are all non-negative and sum to 1.

model.add(Activation('softmax'))

Compiling the model
Keras is built on top of Theano and TensorFlow. Both packages allow you to 
define a computation graph in Python, which then compiles and runs efficiently 
on the CPU or GPU without the overhead of the Python interpreter.

When compiing a model, Keras asks you to specify your loss function and your optimizer. 
The loss function we'll use here is called categorical cross-entropy, and is a loss 
function well-suited to comparing two probability distributions.

Our predictions are probability distributions across the ten different 
digits (e.g. "we're 80% confident this image is a 3, 10% sure it's an 8, 5% it's a 2, etc."),
and the target is a probability distribution with 100% for the correct category, 
and 0 for everything else. The cross-entropy is a measure of how different your predicted 
distribution is from the target distribution. More detail at Wikipedia

The optimizer helps determine how quickly the model learns through gradient descent. 
The rate at which descends a gradient is called the learning rate.



| Topic | Description |
|-------|-------------|
| Core Idea | This is literally where all the MAGIC of learning patterns from data happens! |
| What Gradient Descent Does | Gradient descent identifies how each parameter should be tweaked to reduce the loss in the next iteration. |
| Simplified Explanation | When there's an error between predicted and expected values, each parameter individually tries to correct itself to reduce this error in future iterations. |
| Dialog Metaphor | **Parameter:** “Sorry for the error, what should I change?”<br>**Model:** “Increase/decrease slightly to reduce total loss.”<br>**Parameter:** “Thanks, will do and let’s see next time!” |
| Simultaneous Update | All parameters update together, in appropriate step sizes (learning rate), and eventually converge to a global minimum. |
| Gradient Proportionality | Parameters with higher influence on the loss (higher gradients) are updated more aggressively. |
| Loss Function’s Role | The loss function must provide a scalar that accurately reflects how well/badly the model is performing at the intended task. |
| Incentive Mechanism | The model is "rewarded" when the loss is low (good behavior), and "penalized" heavily when the loss is high (bad behavior). |
| Automation Insight | With a proper loss function and gradient descent, the model can self-improve just by being given correctly labeled training data. |
| Learning Loop Summary | Predict with random weights → fail → calculate loss → adjust weights via gradient descent → repeat → eventually learn the task effectively. |





| Topic | Description |
|-------|-------------|
| Optimizer | **Adam Optimizer** is used for tuning weights. It typically outperforms other optimization algorithms with faster computation and fewer parameters to tune. |
| Loss Function | **Categorical Cross Entropy** penalizes low confidence in correct predictions with high loss, and gives low loss when confidence is near 1. |
| Why Not Accuracy | Accuracy does not reflect the model's confidence. For example, predicting 60% vs 90% confidence for the correct class yields the same accuracy, but very different losses. |
| Role of Gradients | Weight updates are based on **gradients of the loss function**, not on accuracy, since gradients offer more fine-grained feedback. |
| Training Goal | The model is trained to **increase its confidence** in predicting the correct class by minimizing loss — not just making the correct prediction. |



## Train the model
This is the fun part!

The batch size determines over how much data per step is used to compute the loss function, gradients, and back propagation. Large batch sizes allow the network to complete it's training faster; however, there are other factors beyond training speed to consider.

Too large of a batch size smoothes the local minima of the loss function, causing the optimizer to settle in one because it thinks it found the global minimum.

Too small of a batch size creates a very noisy loss function, and the optimizer may never find the global minimum.

So a good batch size may take some trial and error to find!


# Now let's train the model
history = model.fit(X_train, Y_train,validation_data=(X_test, Y_test),
          batch_size=128, epochs=5, verbose=1)
#EPOCH - In terms of artificial neural networks, an epoch refers to one cycle 
through the full training dataset. Usually, training a neural network 
takes more than a few epochs.

#In other words, if we feed a neural network the training data for 
more than one epoch in different patterns, we hope for a better generalization 
when given a new "unseen" input (test data).

The two numbers, in order, represent the value of the loss function of 
the network on the training set, and the overall accuracy of the network on the training data.

We see that The loss goes down and the accuracy improves with time.

But how does it do on data it did not train on?


```

# Function to plot loss
def plot_loss(history):
    plt.plot(history.history['loss'], label='loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.xlabel('Epoch')
    plt.ylabel('Error (Loss)')
    plt.legend()
    plt.grid(True)

plot_loss(history)



```
```
score = model.evaluate(X_test, Y_test)
print('Test score:', score[0])
print('Test accuracy:', score[1])

```


Inspecting the output

It's always a good idea to inspect the output and make sure everything looks sane. 
Here we'll look at some examples it gets right, and some examples it gets wrong.



# The predict_classes function outputs the highest probability class
# according to the trained classifier for each input example.
predicted_classes = np.argmax(model.predict(X_test), axis=-1) 
# we get probabilities for each of the class, and the argmax corresponds 
the class index with the highest probability

# Check which items we got right / wrong
correct_indices = np.nonzero(predicted_classes == y_test)[0]

incorrect_indices = np.nonzero(predicted_classes != y_test)[0]


```

# Let us examine the Correctly labelled images
plt.rcParams['figure.figsize'] = (9,9) # Change these values to Make the figures bigger/smaller
plt.figure()
for i, correct in enumerate(correct_indices[:9]):
    plt.subplot(3,3,i+1)
    plt.imshow(X_test[correct].reshape(28,28), cmap='gray', interpolation='none')
    plt.title(f"Predicted {predicted_classes[correct]}, Class {y_test[correct]}")

plt.tight_layout()

```
```

# Let us examine the InCorrectly  labelled images
plt.figure()
for i, incorrect in enumerate(incorrect_indices[:9]):
    plt.subplot(3,3,i+1)
    plt.imshow(X_test[incorrect].reshape(28,28), cmap='gray', interpolation='none')
    plt.title(f"Predicted {predicted_classes[incorrect]}, Class {y_test[incorrect]}")

plt.tight_layout()


```
```
Trying experimenting with the batch size, Number of layers, number of nodes in each of the layers etc.!
How does increasing the batch size to 10,000 affect the training time and test accuracy?

How about a batch size of 32?

```

Now that The model has been trained, we would like to save it, download it, 
load it and use it for future inferences.

```

# Save model
model.save("trained_model.h5")

# Load the saved model
saved_model = models.load_model('trained_model.h5')


```
```

predicted_classes = np.argmax(model.predict(X_test), axis=-1) # we get probabilities for each of the class, and the argmax corresponds the class index with the highest probability
predicted_classes_from_saved = np.argmax(saved_model.predict(X_test), axis=-1)
(predicted_classes == predicted_classes_from_saved).all()

```


































