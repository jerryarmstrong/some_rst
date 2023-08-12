tests/ui/parser/extern-expected-fn-or-brace.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Verifies that the expected token errors for `extern crate` are raised.

extern "C" mod foo; //~ERROR expected `{`, found keyword `mod`


