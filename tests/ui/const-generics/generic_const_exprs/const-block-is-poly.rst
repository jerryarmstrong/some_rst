tests/ui/const-generics/generic_const_exprs/const-block-is-poly.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(inline_const, generic_const_exprs)]
//~^ WARN the feature `generic_const_exprs` is incomplete

fn foo<T>() {
    let _ = [0u8; const { std::mem::size_of::<T>() }];
    //~^ ERROR: overly complex generic constant
}

fn main() {
    foo::<i32>();
}


