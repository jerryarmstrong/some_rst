tests/ui/type-namespace.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

struct A { a: isize }

fn a(a: A) -> isize { return a.a; }

pub fn main() { let x: A = A {a: 1}; assert_eq!(a(x), 1); }


