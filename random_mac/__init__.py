"""
Use machine learning to identify randomly-generated MAC addresses.
"""


__author__ = "critical-path"

__version__ = "0.7.0"

__all__ = [
  "is_random_mac"
]


from random_mac.classifier import is_random_mac
