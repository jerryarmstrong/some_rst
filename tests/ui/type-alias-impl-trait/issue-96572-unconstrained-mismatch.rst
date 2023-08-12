tests/ui/type-alias-impl-trait/issue-96572-unconstrained-mismatch.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

fn main() {
    type T = impl Copy;
    let foo: T = Some((1u32, 2u32));
    match foo {
        None => (),
        Some((a, b, c)) => (), //~ ERROR mismatched types
    }
}


