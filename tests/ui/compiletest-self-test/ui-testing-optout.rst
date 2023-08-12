tests/ui/compiletest-self-test/ui-testing-optout.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z ui-testing=no

// Line number < 10
type A = B; //~ ERROR

// Line number >=10, <100
type C = D; //~ ERROR



















































































// Line num >=100
type E = F; //~ ERROR

fn main() {}


