tests/ui/feature-gates/feature-gate-trait_upcasting.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {}

trait Bar: Foo {}

impl Foo for () {}

impl Bar for () {}

fn main() {
    let bar: &dyn Bar = &();
    let foo: &dyn Foo = bar;
    //~^ ERROR trait upcasting coercion is experimental [E0658]
}


