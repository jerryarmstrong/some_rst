tests/ui/iterators/ranges.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    for _ in ..10 {}
    //~^ ERROR E0277
    for _ in ..=10 {}
    //~^ ERROR E0277
    for _ in 0..10 {}
    for _ in 0..=10 {}
    for _ in 0.. {}
}


