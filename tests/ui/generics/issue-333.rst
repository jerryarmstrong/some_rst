tests/ui/generics/issue-333.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn quux<T>(x: T) -> T { let f = id::<T>; return f(x); }

fn id<T>(x: T) -> T { return x; }

pub fn main() { assert_eq!(quux(10), 10); }


