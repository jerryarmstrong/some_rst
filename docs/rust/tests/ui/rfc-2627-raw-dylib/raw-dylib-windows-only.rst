tests/ui/rfc-2627-raw-dylib/raw-dylib-windows-only.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-windows
// compile-flags: --crate-type lib
#![cfg_attr(target_arch = "x86", feature(raw_dylib))]
#[link(name = "foo", kind = "raw-dylib")]
//~^ ERROR: link kind `raw-dylib` is only supported on Windows targets
extern "C" {}


