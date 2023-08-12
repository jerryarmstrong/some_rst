tests/ui/recursion_limit/invalid_macro.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![recursion_limit = foo!()] //~ ERROR malformed `recursion_limit` attribute

macro_rules! foo {
    () => {"128"};
}

fn main() {}


