tests/ui/associated-type-bounds/ambiguous-associated-type.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(associated_type_bounds)]

pub struct Flatten<I>
where
    I: Iterator<Item: IntoIterator>,
{
    inner: <I::Item as IntoIterator>::IntoIter,
}

fn main() {}


