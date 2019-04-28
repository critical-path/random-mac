import collections
import os
import sklearn.model_selection
import random_mac


def main():
  # Make a dataset.

  print("making dataset...", end="")
  multiple = 5
  data, labels = random_mac.dataset.make(multiple)
  print("done!")

  # Split the dataset.

  print("splitting dataset...", end="")
  split = sklearn.model_selection.train_test_split(data, labels)
  train_data, test_data, train_labels, test_labels = split
  print("done!")

  # Make, train, and test the classifier.

  print("making, training, and testing classifier...", end="")
  classifier = random_mac.classifier.make()
  classifier = random_mac.classifier.train(classifier, train_data, train_labels)
  score = random_mac.classifier.test(classifier, test_data, test_labels)
  print("done! (score = {}%)".format(str(int(100 * score))))

  # Save the classifier.

  print("saving classifier...", end="")
  random_mac.classifier.save(classifier, "random-mac-classifier.pickled")
  print("done!")

  # Run the classifier with new data.

  print("running classifier against new data...", end="")
  counter = collections.Counter()

  for index in range(100):
    address = os.getrandom(6).hex()
    result = random_mac.classifier.is_random_mac(classifier, address)
    counter[result] += 1

  print("done! (results = {})".format(str(counter)))


if __name__ == "__main__":
  main()
