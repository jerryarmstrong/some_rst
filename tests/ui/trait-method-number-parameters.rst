tests/ui/trait-method-number-parameters.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    fn foo(&mut self, x: i32, y: i32) -> i32;
}

impl Foo for i32 {
    fn foo(
        &mut self, //~ ERROR
        x: i32,
    ) {
    }
}

fn main() {}


