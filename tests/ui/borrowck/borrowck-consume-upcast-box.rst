tests/ui/borrowck/borrowck-consume-upcast-box.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we report an error if an upcast box is moved twice.

trait Foo { fn dummy(&self); }

fn consume(_: Box<dyn Foo>) {
}

fn foo(b: Box<dyn Foo + Send>) {
    consume(b);
    consume(b); //~ ERROR use of moved value
}

fn main() {
}


