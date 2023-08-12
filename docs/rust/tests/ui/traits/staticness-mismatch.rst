tests/ui/traits/staticness-mismatch.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    fn dummy(&self) { }
    fn bar();
}

impl Foo for isize {
    fn bar(&self) {}
    //~^ ERROR method `bar` has a `&self` declaration in the impl, but not in the trait
}

fn main() {}


