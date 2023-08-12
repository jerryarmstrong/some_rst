tests/ui/deriving/deriving-eq-ord-boxed-slice.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#[derive(PartialEq, PartialOrd, Eq, Ord, Debug)]
struct Foo(Box<[u8]>);

pub fn main() {
    let a = Foo(Box::new([0, 1, 2]));
    let b = Foo(Box::new([0, 1, 2]));
    assert_eq!(a, b);
    println!("{}", a != b);
    println!("{}", a < b);
    println!("{}", a <= b);
    println!("{}", a == b);
    println!("{}", a > b);
    println!("{}", a >= b);
}


