tests/ui/associated-types/object-normalization.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-tidy-linelength

// Check that we normalize super predicates for object candidates.

// check-pass

use std::ops::Index;

fn next<'a, T>(s: &'a mut dyn SVec<Item = T, Output = T>) {
    // To prove
    // `dyn SVec<Item = T, Output = T>: SVec`
    // we need to show
    // `dyn SVec<Item = T, Output = T> as Index>::Output == <dyn SVec<Item = T, Output = T> as SVec>::Item`
    // which, with the current normalization strategy, has to be eagerly
    // normalized to:
    // `dyn SVec<Item = T, Output = T> as Index>::Output == T`.
    let _ = s.len();
}

trait SVec: Index<usize, Output = <Self as SVec>::Item> {
    type Item;

    fn len(&self) -> usize;
}

fn main() {}


