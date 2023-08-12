tests/ui/illegal-ufcs-drop.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
struct Foo;

impl Drop for Foo {
    fn drop(&mut self) {}
}

fn main() {
    Drop::drop(&mut Foo) //~ ERROR explicit use of destructor method
}


