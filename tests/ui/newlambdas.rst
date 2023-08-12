tests/ui/newlambdas.rs
======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Tests for the new |args| expr lambda syntax


fn f<F>(i: isize, f: F) -> isize where F: FnOnce(isize) -> isize { f(i) }

fn g<G>(_g: G) where G: FnOnce() { }

pub fn main() {
    assert_eq!(f(10, |a| a), 10);
    g(||());
    assert_eq!(f(10, |a| a), 10);
    g(||{});
}


