tests/ui/lto/lto-thin-rustc-loads-linker-plugin.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -C lto=thin
// aux-build:lto-rustc-loads-linker-plugin.rs
// run-pass
// no-prefer-dynamic

// Same as the adjacent `lto-thin-rustc-loads-linker-plugin.rs` test, only with
// ThinLTO.

extern crate lto_rustc_loads_linker_plugin;

fn main() {
    lto_rustc_loads_linker_plugin::foo();
}


