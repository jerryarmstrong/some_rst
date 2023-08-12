tests/ui/type-alias-impl-trait/cross_inference.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(type_alias_impl_trait)]

fn main() {
    type T = impl Copy;
    let foo: T = (1u32, 2u32);
    let x: (_, _) = foo;
    println!("{:?}", x);
}


