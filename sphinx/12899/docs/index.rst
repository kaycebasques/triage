####################################
Sphinx Bug Heading In Only Directive
####################################

Reproduction of the bug.

H's
===

Subheading
----------

This is a subheading.

.. only:: html

   References
   ----------

   This paragraph is only displayed when generating the HTML output.

.. [CIT] Example citation

This paragraph should be shown *after* the "References" header [CIT]_.

P's
===

.. only:: html

   On the other hand, whenever the :code:`only` directive does **not** include a heading, the order is as expected.

This paragraph is shown after the above, at least for HTML output.
