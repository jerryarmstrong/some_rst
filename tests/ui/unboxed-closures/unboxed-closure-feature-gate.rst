tests/ui/unboxed-closures/unboxed-closure-feature-gate.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that parenthetical notation is feature-gated except with the
// `Fn` traits.

use std::marker;

trait Foo<A> {
    type Output;

    fn dummy(&self, a: A) { }
}

fn main() {
    let x: Box<dyn Foo(isize)>;
    //~^ ERROR parenthetical notation is only stable when used with `Fn`-family

    // No errors with these:
    let x: Box<dyn Fn(isize)>;
    let x: Box<dyn FnMut(isize)>;
    let x: Box<dyn FnOnce(isize)>;
}


