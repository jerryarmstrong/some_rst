tests/ui/parser/extern-foreign-crate.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Verifies that the expected token errors for `extern crate` are
// raised

extern crate foo {} //~ERROR expected one of `;` or `as`, found `{`


