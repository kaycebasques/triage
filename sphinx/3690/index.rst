====
3690
====

.. include:: <isonum.txt>

in the following glossary you should see ``QuickBooks``
followed by the trademark symbol rendered correctly

.. glossary::

   QuickBooks\ |trade|
      foo bar baz

Glossary was defined like this:

.. code-block:: rst

   .. glossary::

      QuickBooks\ |trade|
         foo bar baz

note that trademark symbol is available on this page as ``|trade|`` by including the
`docutils standard definition file <https://docutils.sourceforge.io/docs/ref/rst/definitions.html>`_
``<isonum.txt>``

but on :ref:`genindex` this glossary entry is displayed incorrectly as ``QuickBookstrade``
