Testing random-mac
==================

To conduct testing, run the following command from your shell.

.. code-block:: console

   [user@host random-mac]$ pytest --cov --cov-report=term-missing

If pytest raises an :code:`INTERNALERROR`, then run the following command from your shell.

.. code-block:: console

   [user@host random-mac]$ sudo $(which pytest) --cov --cov-report=term-missing
