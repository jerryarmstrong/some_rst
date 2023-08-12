tests/ui/cfg/cfg-family.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
// pretty-expanded FIXME #23616
// ignore-wasm32-bare no bare family
// ignore-sgx

#[cfg(windows)]
pub fn main() {
}

#[cfg(unix)]
pub fn main() {
}


