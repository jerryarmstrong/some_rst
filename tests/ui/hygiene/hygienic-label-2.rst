tests/ui/hygiene/hygienic-label-2.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! foo {
    ($e: expr) => { 'x: loop { $e } }
}

pub fn main() {
    foo!(break 'x); //~ ERROR use of undeclared label `'x`
}


