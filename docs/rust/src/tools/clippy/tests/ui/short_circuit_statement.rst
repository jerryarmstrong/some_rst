src/tools/clippy/tests/ui/short_circuit_statement.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![warn(clippy::short_circuit_statement)]
#![allow(clippy::nonminimal_bool)]

fn main() {
    f() && g();
    f() || g();
    1 == 2 || g();
}

fn f() -> bool {
    true
}

fn g() -> bool {
    false
}


