tests/ui/array-slice-vec/array-break-length.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    loop {
        |_: [_; break]| {} //~ ERROR: `break` outside of a loop
    }

    loop {
        |_: [_; continue]| {} //~ ERROR: `continue` outside of a loop
    }
}


