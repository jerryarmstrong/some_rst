src/tools/rustfmt/tests/target/configs/disable_all_formatting/false.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-disable_all_formatting: false
// Disable all formatting

fn main() {
    if lorem {
        println!("ipsum!");
    } else {
        println!("dolor!");
    }
}


