tests/ui/impl-trait/rpit-assoc-pair-with-lifetime.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

pub fn iter<'a>(v: Vec<(u32, &'a u32)>) -> impl DoubleEndedIterator<Item = (u32, &u32)> {
    v.into_iter()
}

fn main() {}


