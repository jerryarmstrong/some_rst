tests/ui/or-patterns/issue-64879-trailing-before-guard.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // In this regression test we check that a trailing `|` in an or-pattern just
// before the `if` token of a `match` guard will receive parser recovery with
// an appropriate error message.

enum E { A, B }

fn main() {
    match E::A {
        E::A |
        E::B | //~ ERROR a trailing `|` is not allowed in an or-pattern
        if true => {
            let recovery_witness: bool = 0; //~ ERROR mismatched types
        }
    }
}


