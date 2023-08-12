tests/ui/feature-gates/feature-gate-exclusive-range-pattern.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn main() {
    match 22 {
        0 .. 3 => {} //~ ERROR exclusive range pattern syntax is experimental
        _ => {}
    }
}


