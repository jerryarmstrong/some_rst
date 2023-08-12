tests/ui/mir-unpretty.rs
========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z unpretty=mir

fn main() {
    let x: () = 0; //~ ERROR: mismatched types
}


