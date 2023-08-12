tests/ui/type-alias-impl-trait/destructuring.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

// check-pass

// issue: https://github.com/rust-lang/rust/issues/104551

fn main() {
    type T = impl Sized;
    let (_a, _b): T = (1u32, 2u32);
}


