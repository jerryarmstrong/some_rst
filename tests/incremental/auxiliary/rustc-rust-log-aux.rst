tests/incremental/auxiliary/rustc-rust-log-aux.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustc-env:RUSTC_LOG=debug
#[cfg(rpass1)]
pub fn foo() {}

#[cfg(rpass2)]
pub fn foo() {
    println!();
}


