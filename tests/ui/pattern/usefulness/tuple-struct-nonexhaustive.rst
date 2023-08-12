tests/ui/pattern/usefulness/tuple-struct-nonexhaustive.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo(isize, isize);

fn main() {
    let x = Foo(1, 2);
    match x {   //~ ERROR non-exhaustive
        Foo(1, b) => println!("{}", b),
        Foo(2, b) => println!("{}", b)
    }
}


