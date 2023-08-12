tests/ui/impl-trait/recursive-type-alias-impl-trait-declaration-too-subtle.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

mod a {
    type Foo = impl PartialEq<(Foo, i32)>;
    //~^ ERROR: unconstrained opaque type

    struct Bar;

    impl PartialEq<(Bar, i32)> for Bar {
        fn eq(&self, _other: &(Foo, i32)) -> bool {
            //~^ ERROR: `eq` has an incompatible type for trait
            true
        }
    }
}

mod b {
    type Foo = impl PartialEq<(Foo, i32)>;
    //~^ ERROR: unconstrained opaque type

    struct Bar;

    impl PartialEq<(Foo, i32)> for Bar {
        fn eq(&self, _other: &(Bar, i32)) -> bool {
            //~^ ERROR: `eq` has an incompatible type for trait
            true
        }
    }
}

fn main() {}


