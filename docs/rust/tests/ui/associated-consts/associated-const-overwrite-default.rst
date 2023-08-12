tests/ui/associated-consts/associated-const-overwrite-default.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

trait Foo {
    const ID: i32 = 2;
}

impl Foo for i32 {
    const ID: i32 = 1;
}

fn main() {
    assert_eq!(1, <i32 as Foo>::ID);
}


