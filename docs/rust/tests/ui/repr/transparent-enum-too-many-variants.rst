tests/ui/repr/transparent-enum-too-many-variants.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::mem::size_of;

#[repr(transparent)]
enum Foo { //~ ERROR E0731
    A(u8), B(u8),
}

fn main() {
    println!("Foo: {}", size_of::<Foo>());
}


