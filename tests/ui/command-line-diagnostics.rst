tests/ui/command-line-diagnostics.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test checks the output format without the intermediate json representation
// compile-flags: --error-format=human

pub fn main() {
    let x = 42;
    x = 43;
}


