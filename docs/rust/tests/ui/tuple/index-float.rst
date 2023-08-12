tests/ui/tuple/index-float.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn main() {
    let tuple = (((),),);

    let _ = tuple. 0.0; // OK, whitespace
    let _ = tuple.0. 0; // OK, whitespace

    let _ = tuple./*special cases*/0.0; // OK, comment
}


