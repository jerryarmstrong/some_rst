tests/ui/invalid/invalid-macro-matcher.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused_macros)]

macro_rules! invalid {
    _ => (); //~ ERROR invalid macro matcher
}

fn main() {
}


