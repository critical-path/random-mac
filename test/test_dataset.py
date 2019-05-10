import numpy
import random_mac.dataset
import pytest


def test_get_ieee_assignments_oui(oui_file):
  results = random_mac.dataset.get_ieee_assignments(oui_file)
  assert isinstance(results, list)
  assert len(results) == 1


def test_get_ieee_assignments_cid(cid_file):
  results = random_mac.dataset.get_ieee_assignments(cid_file)
  assert isinstance(results, list)
  assert len(results) == 1


def test_make_hexadecimal_digit_strings_oui(assignments_oui):
  results = random_mac.dataset.make_hexadecimal_digit_strings(assignments_oui)
  digit_string = results[0]
  assert isinstance(results, list)
  assert len(results) == 1
  assert len(digit_string) == 12


def test_make_hexadecimal_digit_strings_cid(assignments_cid):
  results = random_mac.dataset.make_hexadecimal_digit_strings(assignments_cid)
  digit_string = results[0]
  assert isinstance(results, list)
  assert len(results) == 1
  assert len(digit_string) == 12


@pytest.mark.parametrize("number", [1, 10])
def test_make_random_hexadecimal_digit_strings(number):
  results = random_mac.dataset.make_random_hexadecimal_digit_strings(number)
  assert isinstance(results, list)
  assert len(results) == number
  assert all(map(lambda result: len(result) == 12, results))


def test_get_mac_features_oui(digit_strings_oui):
  digit_string = digit_strings_oui[0]
  results = random_mac.dataset.get_mac_features(digit_string)
  assert isinstance(results, tuple)
  assert results == (
    "unique",
    True,
    False,
    False,
    False,
    True,
    True,
    False,
  )


def test_get_mac_features_cid(digit_strings_cid):
  digit_string = digit_strings_cid[0]
  results = random_mac.dataset.get_mac_features(digit_string)
  assert isinstance(results, tuple)
  assert results == (
    "local",
    False,
    True,
    False,
    False,
    True,
    False,
    True,
  )


def test_get_features_with_oui(digit_strings_oui):
  results = random_mac.dataset.get_features(digit_strings_oui)
  assert isinstance(results, list)
  assert len(results) == 1


def test_get_features_with_cid(digit_strings_cid):
  results = random_mac.dataset.get_features(digit_strings_cid)
  assert isinstance(results, list)
  assert len(results) == 1


values = [
  "unique",
  "local",
  "unknown",
  True,
  False
]

def test_normalize_features_oui(features_oui):
  results = random_mac.dataset.normalize_features(features_oui)
  assert isinstance(results, numpy.ndarray)
  assert all(map(lambda value: value not in results.flatten(), values))


def test_normalize_features_cid(features_cid):
  results = random_mac.dataset.normalize_features(features_cid)
  assert isinstance(results, numpy.ndarray)
  assert all(map(lambda value: value not in results.flatten(), values))


@pytest.mark.parametrize(("value", "number"), [(True, 1), (False, 10)])
def test_make_labels(value, number):
  results = random_mac.dataset.make_labels(value, number)
  assert len(results) == number
  assert all(map(lambda result: result == value, results))


def test_normalize_labels_oui(labels_oui):
  results = random_mac.dataset.normalize_labels(labels_oui)
  assert isinstance(results, numpy.ndarray)
  assert len(results) == len(labels_oui)


def test_normalize_labels_cid(labels_cid):
  results = random_mac.dataset.normalize_labels(labels_cid)
  assert isinstance(results, numpy.ndarray)
  assert len(results) == len(labels_cid)


def test_make(oui_file, cid_file):
  results = random_mac.dataset.make(2, oui_file=oui_file, cid_file=cid_file)
  data, labels = results
  assert isinstance(data, numpy.ndarray)
  assert isinstance(labels, numpy.ndarray)
  assert len(data) == 6
  assert len(labels) == 6
