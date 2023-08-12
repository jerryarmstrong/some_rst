tests/ui/rustdoc/cfg-rustdoc.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[cfg(doc)]
pub struct Foo;

fn main() {
    let f = Foo; //~ ERROR
}


