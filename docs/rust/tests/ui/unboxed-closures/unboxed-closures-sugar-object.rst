tests/ui/unboxed-closures/unboxed-closures-sugar-object.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test unboxed closure sugar used in object types.

#![allow(dead_code)]

struct Foo<T,U> {
    t: T, u: U
}

trait Getter<A,R> {
    fn get(&self, arg: A) -> R;
}

struct Identity;
impl<X> Getter<X,X> for Identity {
    fn get(&self, arg: X) -> X {
        arg
    }
}

fn main() {
    let x: &dyn Getter<(i32,), (i32,)> = &Identity;
    let (y,) = x.get((22,));
    assert_eq!(y, 22);
}


