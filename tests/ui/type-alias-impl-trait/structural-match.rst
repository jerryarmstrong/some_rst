tests/ui/type-alias-impl-trait/structural-match.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

type Foo = impl Send;

// This is not structural-match
struct A;

const fn value() -> Foo {
    A
}
const VALUE: Foo = value();

fn test() {
    match VALUE {
        VALUE => (),
        //~^ `Foo` cannot be used in patterns
        _ => (),
    }
}

fn main() {}


