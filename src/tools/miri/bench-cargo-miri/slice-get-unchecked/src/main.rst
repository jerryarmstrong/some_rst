src/tools/miri/bench-cargo-miri/slice-get-unchecked/src/main.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! This is a stripped-down version of the code pattern that causes runtime blowup when printing
//! backtraces in a failed test under cargo miri test with -Zmiri-disable-isolation.
//! See https://github.com/rust-lang/miri/issues/2273

fn main() {
    let x = vec![0u8; 4096];
    let mut i = 0;
    while i < x.len() {
        let _element = unsafe { *x.get_unchecked(i) };
        i += 1;
    }
}


