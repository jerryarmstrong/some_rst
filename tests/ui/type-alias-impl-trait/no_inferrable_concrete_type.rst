tests/ui/type-alias-impl-trait/no_inferrable_concrete_type.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Issue 52985: user code provides no use case that allows a type alias `impl Trait`
// We now emit a 'unconstrained opaque type' error

#![feature(type_alias_impl_trait)]

mod foo {
    pub type Foo = impl Copy;
    //~^ ERROR unconstrained opaque type

    // make compiler happy about using 'Foo'
    pub fn bar(x: Foo) -> Foo {
        x
    }
}

fn main() {
    let _: foo::Foo = std::mem::transmute(0u8);
}


