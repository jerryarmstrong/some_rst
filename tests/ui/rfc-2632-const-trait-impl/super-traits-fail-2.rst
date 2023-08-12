tests/ui/rfc-2632-const-trait-impl/super-traits-fail-2.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_trait_impl)]

// revisions: yy yn ny nn

#[cfg_attr(any(yy, yn), const_trait)]
trait Foo {
    fn a(&self);
}

#[cfg_attr(any(yy, ny), const_trait)]
trait Bar: ~const Foo {}
//[ny,nn]~^ ERROR: ~const can only be applied to `#[const_trait]`

const fn foo<T: Bar>(x: &T) {
    x.a();
    //[yn,yy]~^ ERROR the trait bound
}

fn main() {}


