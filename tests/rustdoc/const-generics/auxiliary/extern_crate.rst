tests/rustdoc/const-generics/auxiliary/extern_crate.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
pub fn extern_fn<const N: usize>() -> impl Iterator<Item = [u8; N]> {
    [[0; N]; N].iter().copied()
}

pub struct ExternTy<const N: usize> {
    pub inner: [u8; N],
}

pub type TyAlias<const N: usize> = ExternTy<N>;

pub trait WTrait<const N: usize, const M: usize> {
    fn hey<const P: usize>() -> usize {
        N + M + P
    }
}


