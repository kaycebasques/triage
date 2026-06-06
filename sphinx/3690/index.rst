====
3690
====

.. include:: <isonum.txt>

On the following line you should see ``QuickBooks`` followed
by the trademark symbol correctly rendered as a symbol
trademark symbol:

QuickBooks\ |trade|

It is written in reST like this:

.. code-block:: rst

   QuickBooks\ |trade|

But in the glossary, when we attempt to use the same reST,
it does not render correctly:

.. glossary::

   QuickBooks\ |trade|
      foo bar baz

Note: This does not reproduce as of Sphinx v9.1.0. It renders
correctly in the glossary.
