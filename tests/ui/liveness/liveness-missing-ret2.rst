tests/ui/liveness/liveness-missing-ret2.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f() -> isize { //~ ERROR mismatched types
    // Make sure typestate doesn't interpret this match expression as
    // the function result
   match true { true => { } _ => {} };
}

fn main() { }


