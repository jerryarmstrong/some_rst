tests/ui/associated-consts/associated-const-inherent-impl.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

struct Foo;

impl Foo {
    const ID: i32 = 1;
}

fn main() {
    assert_eq!(1, Foo::ID);
}


