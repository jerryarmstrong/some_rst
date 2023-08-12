tests/ui/suggestions/assoc-const-as-field.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub mod Mod {
    pub struct Foo {}
    impl Foo {
        pub const BAR: usize = 42;
    }
}

fn foo(_: usize) {}

fn main() {
    foo(Mod::Foo.Bar);
    //~^ ERROR expected value, found
}


