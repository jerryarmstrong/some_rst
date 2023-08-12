tests/ui/structs-enums/tuple-struct-matching.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
struct Foo(isize, isize);

pub fn main() {
    let x = Foo(1, 2);
    match x {
        Foo(a, b) => {
            assert_eq!(a, 1);
            assert_eq!(b, 2);
            println!("{} {}", a, b);
        }
    }
}


