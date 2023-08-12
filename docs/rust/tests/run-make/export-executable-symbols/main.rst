tests/run-make/export-executable-symbols/main.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

fn main() {}

#[no_mangle]
pub fn exported_symbol() -> i8 {
    42
}


