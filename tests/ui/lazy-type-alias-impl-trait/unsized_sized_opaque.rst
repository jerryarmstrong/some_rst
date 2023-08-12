tests/ui/lazy-type-alias-impl-trait/unsized_sized_opaque.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn main() {}

pub struct PairSlices<'a, 'b, T> {
    pub(crate) a0: &'a mut [T],
    pub(crate) a1: &'a mut [T],
    pub(crate) b0: &'b [T],
    pub(crate) b1: &'b [T],
}

impl<'a, 'b, T> PairSlices<'a, 'b, T> {
    pub fn remainder(self) -> impl Iterator<Item = &'b [T]> {
        IntoIterator::into_iter([self.b0, self.b1])
    }
}


