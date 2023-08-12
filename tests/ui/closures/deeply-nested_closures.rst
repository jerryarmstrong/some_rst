tests/ui/closures/deeply-nested_closures.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that this can be compiled in a reasonable time.

// build-pass

fn main() {
    // 96 nested closures
    let x = ();
    || || || || || || || ||
    || || || || || || || ||
    || || || || || || || ||
    || || || || || || || ||

    || || || || || || || ||
    || || || || || || || ||
    || || || || || || || ||
    || || || || || || || ||

    || || || || || || || ||
    || || || || || || || ||
    || || || || || || || ||
    || || || || || || || ||
    [&(), &x];
}


