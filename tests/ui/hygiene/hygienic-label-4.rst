tests/ui/hygiene/hygienic-label-4.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! foo {
    ($e: expr) => { 'x: for _ in 0..1 { $e } }
}

pub fn main() {
    foo!(break 'x); //~ ERROR use of undeclared label `'x`
}


