## random-mac v0.1.0

Use machine learning to identify randomly-generated MAC addresses.


## Dependencies

random-mac requires Python 3.x and the pip package.  It also requires the following packages.

- [macaddress](https://github.com/critical-path/macaddress)
- numpy
- pandas
- scikit-learn


## Installing random-mac

1. Clone or download this repository.

2. Using `sudo`, run `pip` with the `install` command and the `--requirement` option.

```bash
sudo pip install --requirement requirements.txt .
```


## Using random-mac

1. Create, train, test, and save (pickle) a classifier.

```python
>>> import collections
>>> import os
>>> import sklearn.model_selection
>>> import random_mac

# Make a dataset.

>>> multiple = 5
>>> data, labels = random_mac.dataset.make(multiple)

# Split the dataset.

>>> split = sklearn.model_selection.train_test_split(data, labels)
>>> train_data, test_data, train_labels, test_labels = split

# Make, train, and test the classifier.

>>> classifier = random_mac.classifier.make()
>>> classifier = random_mac.classifier.train(classifier, train_data, train_labels)
>>> score = random_mac.classifier.test(classifier, test_data, test_labels)
>>> print("score = {}%".format(str(int(100 * score))))
score = 83%

# Save the classifier.

>>> random_mac.classifier.save(classifier, "random-mac-classifier.pickled")

# Run the classifier with new data.

>>> counter = collections.Counter()
>>> for index in range(100):
...   address = os.getrandom(6).hex()
...   result = random_mac.classifier.is_random_mac(classifier, address)
...   counter[result] += 1
...
>>> print("results = {}".format(str(counter)))
results = Counter({True:100})
```

2. Restore (unpickle) and use the classifier.

```
>>> import random_mac

# Find a MAC address in a host's ARP cache, a switch's MAC address table, etc.

>>> address = "aabbccddeeff"

# Restore and use the classifier.

>>> classifier = random_mac.classifier.restore("random-mac-classifier.pickled")
>>> result = random_mac.classifier.is_random_mac(classifier, address)
>>> print(result)
True
```


## A note on random-mac

To build its dataset, random-mac requires two files not included in this repo.

- [oui.csv](http://standards-oui.ieee.org/oui/oui.csv)
- [cid.csv](http://standards-oui.ieee.org/cid/cid.csv)
