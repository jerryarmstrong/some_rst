tests/ui/type/type-error-break-tail.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn loop_ending() -> i32 {
    loop {
        if false { break; } //~ ERROR mismatched types
        return 42;
    }
}

fn main() {}


