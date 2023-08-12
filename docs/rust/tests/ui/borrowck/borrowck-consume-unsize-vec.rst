tests/ui/borrowck/borrowck-consume-unsize-vec.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we report an error if an upcast box is moved twice.

fn consume(_: Box<[i32]>) {
}

fn foo(b: Box<[i32;5]>) {
    consume(b);
    consume(b); //~ ERROR use of moved value
}

fn main() {
}


