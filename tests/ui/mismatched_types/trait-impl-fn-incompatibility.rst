tests/ui/mismatched_types/trait-impl-fn-incompatibility.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    fn foo(x: u16);
    fn bar(&mut self, bar: &mut Bar);
}

struct Bar;

impl Foo for Bar {
    fn foo(x: i16) { } //~ ERROR incompatible type
    fn bar(&mut self, bar: &Bar) { } //~ ERROR incompatible type
}

fn main() {
}


