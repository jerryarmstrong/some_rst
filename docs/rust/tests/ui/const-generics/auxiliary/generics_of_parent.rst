tests/ui/const-generics/auxiliary/generics_of_parent.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generic_const_exprs)]
#![allow(incomplete_features)]

// library portion of regression test for #87674
pub struct Foo<const N: usize>([(); N + 1])
where
    [(); N + 1]: ;

// library portion of regression test for #87603
pub struct S<T: Copy + Default, const N: usize>
where
    [T; N * 2]: Sized,
{
    pub s: [T; N * 2],
}
impl<T: Default + Copy, const N: usize> S<T, N>
where
    [T; N * 2]: Sized,
{
    pub fn test() -> Self {
        S { s: [T::default(); N * 2] }
    }
}


