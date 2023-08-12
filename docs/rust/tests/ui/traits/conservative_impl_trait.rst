tests/ui/traits/conservative_impl_trait.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)
// #39665

fn batches(n: &u32) -> impl Iterator<Item=&u32> {
    std::iter::once(n)
}

fn main() {}


