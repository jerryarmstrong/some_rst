tests/ui/const-generics/generic_const_exprs/drop_impl.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //check-pass
#![feature(generic_const_exprs)]
#![allow(incomplete_features)]

struct Foo<const N: usize>
where
    [(); N + 1]: ;

impl<const N: usize> Drop for Foo<N>
where
    [(); N + 1]: ,
{
    fn drop(&mut self) {}
}

fn main() {}


