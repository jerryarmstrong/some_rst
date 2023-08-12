tests/ui/self/self-vs-path-ambiguity.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that `self::foo` is parsed as a general pattern and not a self argument.

struct S;

impl S {
    fn f(self::S: S) {}
    fn g(&self::S: &S) {}
    fn h(&mut self::S: &mut S) {}
    fn i(&'a self::S: &S) {} //~ ERROR unexpected lifetime `'a` in pattern
}

fn main() {}


