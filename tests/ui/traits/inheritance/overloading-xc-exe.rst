tests/ui/traits/inheritance/overloading-xc-exe.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:overloading_xc.rs


extern crate overloading_xc;
use overloading_xc::{MyNum, MyInt};

fn f<T:MyNum>(x: T, y: T) -> (T, T, T) {
    return (x.clone() + y.clone(), x.clone() - y.clone(), x * y);
}

fn mi(v: isize) -> MyInt { MyInt { val: v } }

pub fn main() {
    let (x, y) = (mi(3), mi(5));
    let (a, b, c) = f(x, y);
    assert_eq!(a, mi(8));
    assert_eq!(b, mi(-2));
    assert_eq!(c, mi(15));
}


