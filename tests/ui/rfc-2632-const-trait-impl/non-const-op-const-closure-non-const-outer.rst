tests/ui/rfc-2632-const-trait-impl/non-const-op-const-closure-non-const-outer.rs
================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_closures, const_trait_impl)]
#![allow(incomplete_features)]

trait Foo {
    fn foo(&self);
}

impl Foo for () {
    fn foo(&self) {}
}

fn main() {
    (const || { (()).foo() })();
    //~^ ERROR: cannot call non-const fn
}


