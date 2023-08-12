tests/ui/recursion_limit/invalid_digit_type.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![recursion_limit = 123] //~ ERROR malformed `recursion_limit` attribute

fn main() {}


