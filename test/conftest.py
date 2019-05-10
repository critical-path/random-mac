import random_mac
import pytest


# This fixture approximates `oui.csv`.

@pytest.fixture
def oui_file(tmp_path):
  # Create a temporary subdirectory if one does not already exist.
  subdirectory = tmp_path.joinpath("subdirectory")

  try:
    subdirectory.mkdir()
  except FileExistsError:
    pass

  # Create a temporary file in the subdirectory.
  file = subdirectory.joinpath("oui.csv")
  file.write_text("Assignment,\na0b1c2,\n")

  # Yield the file.
  yield file


# This fixture approximates `cid.csv`.

@pytest.fixture
def cid_file(tmp_path):
  # Create a temporary subdirectory if one does not already exist.
  subdirectory = tmp_path.joinpath("subdirectory")

  try:
    subdirectory.mkdir()
  except FileExistsError:
    pass

  # Create a temporary file in the subdirectory.
  file = subdirectory.joinpath("cid.csv")
  file.write_text("Assignment,\n0a1b2c,\n")

  # Yield the file.
  yield file


# This fixture represents the output of 
# `random_mac.dataset.get_ieee_assignments`.

@pytest.fixture
def assignments_oui(oui_file):
  return random_mac.dataset.get_ieee_assignments(oui_file)


# This fixture represents the output of 
# `random_mac.dataset.get_ieee_assignments`.

@pytest.fixture
def assignments_cid(cid_file):
  return random_mac.dataset.get_ieee_assignments(cid_file)


# This fixture represents the output of
# `random_mac.dataset.make_hexadecimal_digit_strings`.

@pytest.fixture
def digit_strings_oui(assignments_oui):
  return random_mac.dataset.make_hexadecimal_digit_strings(assignments_oui)


# This fixture represents the output of
# `random_mac.dataset.make_hexadecimal_digit_strings`.

@pytest.fixture
def digit_strings_cid(assignments_cid):
  return random_mac.dataset.make_hexadecimal_digit_strings(assignments_cid)


# This fixture represents the output of
# `random_mac.dataset.normalize_features`.

@pytest.fixture
def features_oui(digit_strings_oui):
  return random_mac.dataset.normalize_features(digit_strings_oui)


# This fixture represents the output of 
# `random_mac.dataset.normalize_features`.

@pytest.fixture
def features_cid(digit_strings_cid):
  return random_mac.dataset.normalize_features(digit_strings_cid)


# This fixture represents the output of `random_mac.dataset.make_labels`.

@pytest.fixture
def labels_oui(features_oui):
  return random_mac.dataset.make_labels(False, 1)


# This fixture represents the output of `random_mac.dataset.make_labels`.

@pytest.fixture
def labels_cid(features_cid):
  return random_mac.dataset.make_labels(False, 1)


# This fixture represents the output of `random_mac.dataset.make`.

@pytest.fixture
def dataset(oui_file, cid_file):
  return random_mac.dataset.make(2, oui_file=oui_file, cid_file=cid_file)


# This fixture represents the output of `random_mac.classifier.make`.

@pytest.fixture
def unfitted_classifier():
  return random_mac.classifier.make()


# This fixture represents the output of `random_mac.classifier.train`.

@pytest.fixture
def fitted_classifier(unfitted_classifier, dataset):
  data, labels = dataset
  return random_mac.classifier.train(unfitted_classifier, data, labels)


# This fixture provides a temporary a path to a pickle file.

@pytest.fixture
def pickle_file(tmp_path):
  # Create a temporary subdirectory if one does not already exist.
  subdirectory = tmp_path.joinpath("subdirectory")

  try:
    subdirectory.mkdir()
  except FileExistsError:
    pass

  # Create a path to the pickle file.
  file = subdirectory.joinpath("test-classifier.pickled")

  # Yield the path to the pickle file.
  yield file
