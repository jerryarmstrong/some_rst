tests/ui/wf/hir-wf-check-erase-regions.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #87549.
// incremental

pub struct Table<T, const N: usize>([Option<T>; N]);

impl<'a, T, const N: usize> IntoIterator for &'a Table<T, N> {
    type IntoIter = std::iter::Flatten<std::slice::Iter<'a, T>>; //~ ERROR `&T` is not an iterator
    type Item = &'a T;

    fn into_iter(self) -> Self::IntoIter { //~ ERROR `&T` is not an iterator
        unimplemented!()
    }
}
fn main() {}


