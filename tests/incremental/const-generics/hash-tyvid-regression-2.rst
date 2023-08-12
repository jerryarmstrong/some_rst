tests/incremental/const-generics/hash-tyvid-regression-2.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: cfail
#![feature(generic_const_exprs, adt_const_params)]
#![allow(incomplete_features)]
// regression test for #77650
struct C<T, const N: core::num::NonZeroUsize>([T; N.get()])
where
    [T; N.get()]: Sized;
impl<'a, const N: core::num::NonZeroUsize, A, B: PartialEq<A>> PartialEq<&'a [A]> for C<B, N>
where
    [B; N.get()]: Sized,
{
    fn eq(&self, other: &&'a [A]) -> bool {
        self.0 == other
        //~^ error: can't compare
    }
}

fn main() {}


