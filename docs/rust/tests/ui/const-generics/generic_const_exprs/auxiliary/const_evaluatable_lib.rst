tests/ui/const-generics/generic_const_exprs/auxiliary/const_evaluatable_lib.rs
==============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generic_const_exprs)]
#![allow(incomplete_features)]

pub fn test1<T>() -> [u8; std::mem::size_of::<T>() - 1]
where
    [u8; std::mem::size_of::<T>() - 1]: Sized,
{
    [0; std::mem::size_of::<T>() - 1]
}


