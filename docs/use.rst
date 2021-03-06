Using random-mac
================

Getting started
---------------

random-mac requires lists of organzationally-unique identifiers (OUI) and company IDs (CID) assigned by the IEEE.  To fetch them from the IEEE's website, run the following commands from your shell.

.. code-block:: console

   [user@host random-mac]$ curl http://standards-oui.ieee.org/oui/oui.csv > oui.csv
   [user@host random-mac]$ curl http://standards-oui.ieee.org/cid/cid.csv > cid.csv

Making a dataset
----------------

random-mac's dataset consists of data (samples) and labels (targets).  The data include one non-random MAC address for every OUI and CID assigned by the IEEE (currently about 26,000) as well as a configurable number of random MAC addresses.  To make a dataset with two random MAC addresses for every non-random address (a 2:1 ratio), run the following command from your Python interpreter.

(Use the ratio that is most appropriate for your needs.  Different ratios require different trade-offs.  To get a sense of these trade-offs, use scikit-learn's classification reports.)

.. code-block:: python

   >>> import sklearn.model_selection
   >>> import random_mac
   >>> data, labels = random_mac.dataset.make(
   ...   2,
   ...   oui_file="./oui.csv",
   ...   cid_file="./cid.csv"
   ... )

Splitting the dataset
---------------------

random-mac needs to use some data and labels for training while reserving others for testing.  To split data and labels into two different groups, run the following command from your Python interpreter.

.. code-block:: python

   >>> training_data, testing_data, training_labels, testing_labels = sklearn.model_selection.train_test_split(data, labels)

Making a classifier
-------------------

random-mac uses a binary classifier.  To make, train, and test this classifier, run the following commands from your Python interpreter.

.. code-block:: python

   >>> classifier = random_mac.classifier.make()
   >>> classifier = random_mac.classifier.train(
   ...   classifier, 
   ...   training_data, 
   ...   training_labels
   ... )
   >>> score = random_mac.classifier.test(
   ...   classifier, 
   ...   testing_data, 
   ...   testing_labels
   ... )
   >>> print("score = {}%".format(str(int(100 * score))))
   score = 83%

Using the classifier
------------------

To use the classifier, run the following command from your Python interpreter.

.. code-block:: python

   >>> address = "a0b1c2d3e4f5"
   >>> results = random_mac.is_random_mac(classifier, address)
   >>> print(results)
   True

Saving and restoring a classifier
---------------------------------

To save (pickle) a classifier for future use, run the following command from your Python interpreter.

.. code-block:: python

   >>> random_mac.classifier.save(
   ...   classifier,
   ...   file="./random-mac-classifier.pickled" 
   ... )

To restore (unpickle) a classifier, run the following command from your Python interpreter.

.. code-block:: python

   >>> classifier = random_mac.classifier.restore(
   ...   file="./random-mac-classifier.pickled"
   ... )
