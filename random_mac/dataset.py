"""
This module contains dataset-related functions.
"""


import csv
import itertools
import os
import macaddress
import numpy
import pandas


def get_ieee_assignments(file):
  """
  Retrieve OUIs and CIDs.

  Parameters
  ----------
  file : str
    The name of a file with information on OUIs
    and CIDs assigned by the IEEE.

    Typical names are `oui.csv` and `cid.csv`.

  Returns
  -------
  n/a : list
    A list of 24-bit OUIs or CIDs assigned by the IEEE.
  """

  with open(file) as source:
    records = csv.DictReader(source)
    return list(
      map(
        lambda record: record["Assignment"], 
        records
      )
    )


def make_hexadecimal_digit_strings(assignments):
  """
  Make hexadecimal strings based upon OUIs and CIDs.

  Parameters
  ----------
  assignments : list
    A list of 24-bit OUIs or CIDs assigned by the IEEE.

  Returns
  -------
  n/a : list
    A list of 48-bit hexadecimal strings, where each
    string is the concatenation of a 24-bit OUI/CID and
    24 random bits.
  """

  return list(
    map(
      lambda assignment: assignment + os.urandom(3).hex(),
      assignments
    )
  )


def make_random_hexadecimal_digit_strings(number):
  """
  Make random hexadecimal strings.

  Parameters
  ----------
  number : int
    The number of hexadecimal strings to make.

  Returns
  -------
  n/a : list
    A list of 48-bit hexadecimal strings, where each
    string is 48 random bits.
  """

  return list(
    map(
      lambda x: os.urandom(6).hex(),
      range(number)
    )
  )


def get_mac_features(digit_string):
  """
  Retrieve the features of a MAC address.

  Parameters
  ----------
  digit_string : str
    A 48-bit hexadecimal string with which
    to instantiate `MediaAccessControlAddress`.

  Returns
  -------
  n/a : tuple
    A six-tuple with the features of a MAC address.

    The features are `type`, `has_oui`, `has_cid`, 
    `is_broadcast`, `is_multicast`, `is_unicast`,
    `is_uaa`, and `is_laa`.
  """

  mac = macaddress.MediaAccessControlAddress(digit_string)
  return (
    mac.type,
    mac.has_oui,
    mac.has_cid,
    mac.is_broadcast,
    mac.is_multicast,
    mac.is_unicast,
    mac.is_uaa,
    mac.is_laa
  )


def get_features(digit_strings):
  """
  Retrieve the features of MAC addresses.

  Parameters
  ----------
  digit_strings : list
    A list of 48-bit hexadecimal strings.

  Returns
  -------
  n/a : list
    A list of tuples, where each tuple contains 
    the features of a MAC address.
  """

  return list(
    map(
      lambda digit_string: get_mac_features(digit_string),
      digit_strings
    )
  )


def normalize_features(features):
  """
  Normalize the features of MAC addresses.

  Parameters
  ----------
  features : list
    A list of tuples, where each tuple contains 
    the features of a MAC address.

  Returns
  -------
  n/a : numpy array
    A numpy array with the normalized features
    of MAC addresses, where normalization
    means replacing non-numeric with numeric
    values and converting the container from a
    list to a numpy array.
  """

  replacements = {
    "unique": 2,
    "local": 1,
    "unknown": 0,
    True: 1,
    False: 0
  }

  return pandas.DataFrame(features).replace(replacements).to_numpy()

  
def make_labels(value, number):
  """
  Make labels for training and testing of
  a binary classifier.

  Parameters
  ----------
  value : int
    The label, where `0` means a non-random
    MAC addresses and `1` means a random
    MAC address.

  number :
    The number of labels.

  Returns
  -------
  n/a : list
    A list with the given number of the
    given label.  
  """

  return list(
    itertools.repeat(
      value,
      number
    )
  )


def normalize_labels(labels):
  """
  Normalize labels.

  Parameters
  ----------
  labels : list
    A list of labels.

  Returns
  -------
  n/a : numpy array
    A numpy array with normalized labels, 
    where normalization means converting the 
    container from a list to a numpy array.
  """

  return numpy.array(labels)


def make(multiple, oui_file="./oui.csv", cid_file="./cid.csv"):
  """
  Make a dataset for training and testing purposes.

  Parameters
  ----------
  multiple : int
    The number of random MAC addresses to create
    for every non-random MAC address.

  Returns
  -------
  n/a : tuple
    A tuple with data (features) and labels.
  """

  # Get OUIs and CIDs.
  ouis = get_ieee_assignments(oui_file)
  cids = get_ieee_assignments(cid_file)

  # Make non-random and random hexadecimal strings.
  digits = make_hexadecimal_digit_strings(ouis + cids)
  random_digits = make_random_hexadecimal_digit_strings(
    int(multiple * len(digits))
  )

  # Get features of non-random and random MAC addresses.
  features = get_features(digits)
  random_features = get_features(random_digits)

  # Get labels for non-random and random MAC addresses.
  labels = make_labels(0, len(features))
  random_labels = make_labels(1, len(random_features))

  # Normalize all features and labels.
  normalized_features = normalize_features(features + random_features)  
  normalized_labels = normalize_labels(labels + random_labels)

  # Return normalized features and labels.
  return (
    normalized_features,
    normalized_labels,
  )
