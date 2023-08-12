tests/ui/structs-enums/tuple-struct-destructuring.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
struct Foo(isize, isize);

pub fn main() {
    let x = Foo(1, 2);
    let Foo(y, z) = x;
    println!("{} {}", y, z);
    assert_eq!(y, 1);
    assert_eq!(z, 2);
}


