import os
import numpy
import random_mac.classifier
import sklearn.linear_model
import sklearn.utils.validation
import pytest


def test_make():
  results = random_mac.classifier.make()
  assert isinstance(results, sklearn.linear_model.SGDClassifier)


def test_train(unfitted_classifier, dataset):
  data, labels = dataset
  results = random_mac.classifier.train(unfitted_classifier, data, labels)
  assert isinstance(results, sklearn.linear_model.SGDClassifier)
  assert sklearn.utils.validation.check_is_fitted(results, "t_") == None


@pytest.mark.parametrize(
  ("data", "labels"),
  [
    (numpy.array([2, 1, 0, 0, 0, 1, 1, 0]).reshape(1, -1), numpy.array([0])),
    (numpy.array([1, 0, 1, 0, 0, 1, 0, 1]).reshape(1, -1), numpy.array([0]))
  ]
)
def test_test(fitted_classifier, data, labels):
  results = random_mac.classifier.test(fitted_classifier, data, labels)
  assert isinstance(results, float)


def test_save_and_restore(fitted_classifier, pickle_file):
  random_mac.classifier.save(fitted_classifier, file=pickle_file)
  assert pickle_file.exists()
  assert pickle_file.is_file()

  results = random_mac.classifier.restore(file=pickle_file)
  assert isinstance(results, sklearn.linear_model.SGDClassifier)


def test_is_random_mac(fitted_classifier):
  results = random_mac.classifier.is_random_mac(
    fitted_classifier, 
    os.urandom(6).hex()
  )
  assert isinstance(results, bool)
