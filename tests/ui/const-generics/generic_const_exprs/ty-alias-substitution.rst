tests/ui/const-generics/generic_const_exprs/ty-alias-substitution.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// Test that we correctly substitute generic arguments for type aliases.
#![feature(generic_const_exprs)]
#![allow(incomplete_features)]

type Alias<T, const N: usize> = [T; N + 1];

fn foo<const M: usize>() -> Alias<u32, M>  where [u8; M + 1]: Sized {
    [0; M + 1]
}

fn main() {
    foo::<0>();
}


