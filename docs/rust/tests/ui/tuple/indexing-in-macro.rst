tests/ui/tuple/indexing-in-macro.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

macro_rules! m {
    (.$l:literal) => {};
}

m!(.0.0); // OK, `0.0` after a dot is still a float token.

fn main() {}


