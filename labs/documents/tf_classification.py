from __future__ import absolute_import, division, print_function, unicode_literals

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
import cv2

print(tf.__version__)

fashion_mnist = keras.datasets.fashion_mnist
try:
  shirt = Image.open('../images/shirt_grey.jpg')
  np_shirt = np.array(shirt)
  print(np_shirt.shape)
  # shirtx = np.array(shirt.getdata()).reshape(shirt.size[0], shirt.size[1], 1)
  sandal = Image.open('../images/sandal_grey.jpg')
  np_sandal = np.array(sandal)
  # sandalx = np.array(sandal.getdata()).reshape(sandal.size[0], sandal.size[1], 1)
  coat = Image.open('../images/coat_grey.jpeg')
  np_coat = np.array(coat)
  # coatx = np.array(coat.getdata()).reshape(coat.size[0], coat.size[1], 1)
#   shirt = cv2.imread('../images/shirt_grey.jpg')
#   sandal = cv2.imread('../images/sandal_grey.jpg')
#   coat = cv2.imread('../images/coat_grey.jpg')
except IOError:
  pass



(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
test_images = np.array([np_shirt, np_sandal, np_coat])
test_labels = np.array([0, 5, 4])
# test_images = np.append(test_images, np_shirt )
# test_images = np.append(test_images, np_sandal )
# test_images = np.append(test_images, np_coat )
# test_labels = np.append(test_labels, 0 )
# test_labels = np.append(test_labels, 5 )
# test_labels = np.append(test_labels, 4 )

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

def plot_image(i, predictions_array, true_label, img):
  predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  
  plt.imshow(img, cmap=plt.cm.binary)
  
  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'
  
  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array[i], true_label[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)
  
  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

# print(train_images.shape)
# print(len(train_labels))
# print(train_labels)

# print(test_images.shape)
# print(len(test_labels))

# plt.figure(figsize=(10,10))
# for i in range(25):
#     plt.subplot(5,5,i+1)
#     plt.xticks([])
#     plt.yticks([])
#     plt.grid(False)
#     plt.imshow(train_images[i], cmap=plt.cm.binary)
#     plt.xlabel(class_names[train_labels[i]])
# plt.show()

train_images = train_images / 255.0
test_images = test_images / 255.0
# shirtx = shirtx / 255.0
# sandalx = sandalx / 255.0
# coatx = coatx / 255.0

# plt.figure()
# plt.imshow(train_images[0])
# plt.colorbar()
# plt.grid(False)
# plt.show()

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)

test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test accuracy:', test_acc)

predictions = model.predict(test_images)
# print(np.argmax(predictions[0]))

# i = 0
# plt.figure(figsize=(6,3))
# plt.subplot(1,2,1)
# plot_image(i, predictions, test_labels, test_images)
# plt.subplot(1,2,2)
# plot_value_array(i, predictions,  test_labels)
# plt.show()

# i = 12
# plt.figure(figsize=(6,3))
# plt.subplot(1,2,1)
# plot_image(i, predictions, test_labels, test_images)
# plt.subplot(1,2,2)
# plot_value_array(i, predictions,  test_labels)
# plt.show()

# # Plot the first X test images, their predicted label, and the true label
# # Color correct predictions in blue, incorrect predictions in red
# num_rows = 5
# num_cols = 3
# num_images = num_rows*num_cols
# plt.figure(figsize=(2*2*num_cols, 2*num_rows))
# for i in range(9000, num_images + 9000, 1):
#   plt.subplot(num_rows, 2*num_cols, 2*(i-9000)+1)
#   plot_image(i, predictions, test_labels, test_images)
#   plt.subplot(num_rows, 2*num_cols, 2*(i-9000)+2)
#   plot_value_array(i, predictions, test_labels)
# plt.show()

num_rows = 1
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(0, num_images, 1):
  plt.subplot(num_rows, 2*num_cols, 2*(i)+1)
  plot_image(i, predictions, test_labels, test_images)
  plt.subplot(num_rows, 2*num_cols, 2*(i)+2)
  plot_value_array(i, predictions, test_labels)
plt.show()

# Grab an image from the test dataset
img = test_images[0]
# print(img.shape)

# Add the image to a batch where it's the only member.
img = (np.expand_dims(img,0))
# print(img.shape)

predictions_single = model.predict(img)
# print(predictions_single)

# plot_value_array(0, predictions_single, test_labels)
# plt.xticks(range(10), class_names, rotation=45)
# plt.show()

# prediction_result = np.argmax(predictions_single[0])
# print(prediction_result)
