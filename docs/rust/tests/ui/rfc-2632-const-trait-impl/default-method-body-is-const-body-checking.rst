tests/ui/rfc-2632-const-trait-impl/default-method-body-is-const-body-checking.rs
================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_trait_impl)]

#[const_trait]
trait Tr {}
impl Tr for () {}

const fn foo<T>() where T: ~const Tr {}

#[const_trait]
pub trait Foo {
    fn foo() {
        foo::<()>();
        //~^ ERROR the trait bound `(): ~const Tr` is not satisfied
    }
}

fn main() {}


