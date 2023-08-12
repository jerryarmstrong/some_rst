tests/ui/associated-types/associated-types-basic.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
trait Foo {
    type T;
}

impl Foo for i32 {
    type T = isize;
}

fn main() {
    let x: <i32 as Foo>::T = 22;
    let y: isize = 44;
    assert_eq!(x * 2, y);
}


