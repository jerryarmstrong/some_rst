tests/ui/type-alias-impl-trait/type-alias-impl-trait-with-cycle-error.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

type Foo = impl Fn() -> Foo;
//~^ ERROR: unconstrained opaque type

fn crash(x: Foo) -> Foo {
    x
}

fn main() {

}


