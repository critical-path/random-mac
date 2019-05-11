import collections
import os
import sklearn.model_selection
import random_mac


def main():
  # Make a dataset.
  #
  # We use the `multiple` argument to make two
  # randomly-generated MAC addresses for every 
  # non-randomly-generated one.

  multiple = 2
  dataset = random_mac.dataset.make(
    multiple, 
    oui_file="./oui.csv", 
    cid_file="./cid.csv"
  )
  data, labels = dataset

  # Split the dataset.

  split = sklearn.model_selection.train_test_split(data, labels)
  train_data, test_data, train_labels, test_labels = split

  # Make, train, and test the classifier.

  classifier = random_mac.classifier.make()
  classifier = random_mac.classifier.train(classifier, train_data, train_labels)
  score = random_mac.classifier.test(classifier, test_data, test_labels)
  print("score = {}%".format(str(int(100 * score))))

  # Save the classifier.

  random_mac.classifier.save(
    classifier, 
    file="./random-mac-classifier.pickled"
  )

  # Run the classifier with new data.

  counter = collections.Counter()

  for index in range(100):
    address = os.urandom(6).hex()
    result = random_mac.is_random_mac(classifier, address)
    counter[result] += 1

  print("results = {}".format(str(counter)))


if __name__ == "__main__":
  main()
