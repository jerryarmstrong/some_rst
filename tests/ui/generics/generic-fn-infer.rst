tests/ui/generics/generic-fn-infer.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass




// Issue #45: infer type parameters in function applications

fn id<T>(x: T) -> T { return x; }

pub fn main() { let x: isize = 42; let y: isize = id(x); assert_eq!(x, y); }


