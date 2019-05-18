Installing random-mac
=====================

random-mac is available on GitHub at https://github.com/critical-path/random-mac.  

If you do not have pip version 18.1 or higher, then run the following command from your shell.

.. code-block:: console

   [user@host ~]$ sudo pip install --upgrade pip

To install random-mac with test-related dependencies, run the following command from your shell.

.. code-block:: console

   [user@host ~]$ sudo pip install --editable git+https://github.com/critical-path/random-mac.git#egg=random-mac[test]

To install it without test-related dependencies, run the following command from your shell.

.. code-block:: console

   [user@host ~]$ sudo pip install git+https://github.com/critical-path/random-mac.git

(If necessary, replace :code:`pip` with :code:`pip3`.)
