tests/ui/typeck/issue-83621-placeholder-static-in-extern.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #83621.

extern "C" {
    static x: _; //~ ERROR: [E0121]
}

fn main() {}


