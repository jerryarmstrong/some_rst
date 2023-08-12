tests/ui/rfc-2632-const-trait-impl/const-check-fns-in-const-impl.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_trait_impl)]

struct S;
#[const_trait]
trait T {
    fn foo();
}

fn non_const() {}

impl const T for S {
    fn foo() { non_const() }
    //~^ ERROR cannot call non-const fn
}

fn main() {}


