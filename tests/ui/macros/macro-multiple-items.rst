tests/ui/macros/macro-multiple-items.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
macro_rules! make_foo {
    () => (
        struct Foo;

        impl Foo {
            fn bar(&self) {}
        }
    )
}

make_foo!();

pub fn main() {
    Foo.bar()
}


