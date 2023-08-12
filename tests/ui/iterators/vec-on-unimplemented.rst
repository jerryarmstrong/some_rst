tests/ui/iterators/vec-on-unimplemented.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    vec![true, false].map(|v| !v).collect::<Vec<_>>();
    //~^ ERROR `Vec<bool>` is not an iterator
}


