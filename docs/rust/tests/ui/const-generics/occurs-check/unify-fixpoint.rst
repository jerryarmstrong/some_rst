tests/ui/const-generics/occurs-check/unify-fixpoint.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(generic_const_exprs)] //~ WARN the feature `generic_const_exprs` is incomplete


fn bind<const N: usize>(value: [u8; N + 2]) -> [u8; N * 2] {
    todo!()
}

fn main() {
    let mut arr = Default::default();
    arr = bind::<2>(arr);
}


