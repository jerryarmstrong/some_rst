tests/ui/cfg/cfg-target-family.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
// ignore-sgx

// pretty-expanded FIXME #23616

#[cfg(target_family = "windows")]
pub fn main() {}

#[cfg(target_family = "unix")]
pub fn main() {}

#[cfg(all(target_family = "wasm", not(target_os = "emscripten")))]
pub fn main() {}


