"""
This module contains classifier-related functions.
"""


import pickle
import sklearn.linear_model
import random_mac.dataset


def make():
  """
  Retrieve a classifier.

  Returns
  -------
  n/a : sklearn classifier
    A classifier.
  """

  return sklearn.linear_model.SGDClassifier(max_iter=1000, tol=1e-3)


def train(classifier, data, labels):
  """
  Train a classifier.

  Parameters
  ----------
  classifier : sklearn classifier
    The classifier to train.

  data : numpy array
    The data with which to train the 
    classifier.

  labels : numpy array
    The labels with which to train the 
    classifier.

  Returns
  ------
  n/a : sklearn classifier
    The trained classifier.
  """

  return classifier.fit(data, labels)


def test(classifier, data, labels):
  """
  Test a classifier.

  Parameters
  ----------
  classifier : sklearn classifier
    The classifier to test.

  data : numpy array
    The data with which to test the 
    classifier.

  labels : numpy array
    The labels with which to test the
    the classifier.

  Returns
  ------
  n/a : float
    The results of the test.
  """

  return classifier.score(data, labels)


def save(classifier, file):
  """
  Save (pickle) a classifier.

  Parameters
  ----------
  classifier : sklearn classifier
    The classifier to save.

  file : str
    The name of the destination file.
  """

  with open(file, "wb") as destination:
    pickle.dump(classifier, destination)    


def restore(file):
  """
  Restore (unpickle) a classifier.

  Parameters
  ----------
  file : str
    The name of the source file.

  Returns
  -------
  n/a : sklearn classifier
    The restored (unpickled) classifier.
  """

  with open(file, "rb") as source:
    return pickle.load(source)


def is_random_mac(classifier, address):
  """
  Determine whether a MAC address is
  random or non-random.

  Parameters
  ----------
  classifier : sklearn classifier
    The classifier to use.

  address: str (hexadecimal)
    The address to test.

  Returns
  -------
  n/a : bool
    Whether the given MAC address is random
    (True) or non-random (False).
  """

  features = random_mac.dataset.get_mac_features(address)
  normalized = random_mac.dataset.normalize_features(features)
  result = classifier.predict(normalized.reshape(1, -1))

  if result == 1:
    return True
  elif result == 0:
    return False
