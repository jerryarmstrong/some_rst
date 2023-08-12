tests/ui/binding/expr-match-panic-all.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass



// When all branches of a match expression result in panic, the entire
// match expression results in panic.

pub fn main() {
    let _x =
        match true {
          true => { 10 }
          false => { match true { true => { panic!() } false => { panic!() } } }
        };
}


