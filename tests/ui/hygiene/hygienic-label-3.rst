tests/ui/hygiene/hygienic-label-3.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! foo {
    () => { break 'x; } //~ ERROR use of undeclared label `'x`
}

pub fn main() {
    'x: for _ in 0..1 {
        foo!();
    };
}


