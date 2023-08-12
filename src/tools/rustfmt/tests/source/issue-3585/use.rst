src/tools/rustfmt/tests/source/issue-3585/use.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-inline_attribute_width: 100

#[macro_use]
use static_assertions;

#[cfg(unix)]
use static_assertions;


