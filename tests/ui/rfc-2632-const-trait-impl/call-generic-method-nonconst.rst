tests/ui/rfc-2632-const-trait-impl/call-generic-method-nonconst.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_trait_impl)]

struct S;

#[const_trait]
trait Foo {
    fn eq(&self, _: &Self) -> bool;
}

impl Foo for S {
    fn eq(&self, _: &S) -> bool {
        true
    }
}

const fn equals_self<T: ~const Foo>(t: &T) -> bool {
    true
}

// Calling `equals_self` with something that has a non-const impl should throw an error, despite
// it not using the impl.

pub const EQ: bool = equals_self(&S);
//~^ ERROR

fn main() {}


