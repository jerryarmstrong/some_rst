tests/ui/parser/if-block-unreachable-expr.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// This regressed from 1.20 -> 1.21 -- the condition is unreachable,
// but it's still an expression, and should parse fine.

fn main() {
    if { if true { return; } else { return; }; } {}
}


