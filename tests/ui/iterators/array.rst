tests/ui/iterators/array.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn main() {
    for _ in [1, 2] {}
    let x = [1, 2];
    for _ in x {}
    for _ in [1.0, 2.0] {}
}


