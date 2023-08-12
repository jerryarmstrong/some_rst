tests/ui/unconstrained-none.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Issue #5062

fn main() {
    None; //~ ERROR type annotations needed [E0282]
}


