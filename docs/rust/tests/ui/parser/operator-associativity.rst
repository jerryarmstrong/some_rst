tests/ui/parser/operator-associativity.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Testcase for issue #130, operator associativity.

pub fn main() { assert_eq!(3 * 5 / 2, 7); }


