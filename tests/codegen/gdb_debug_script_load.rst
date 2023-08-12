tests/codegen/gdb_debug_script_load.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //
// ignore-windows
// ignore-macos
// ignore-wasm
// ignore-emscripten

// compile-flags: -g -C no-prepopulate-passes

#![feature(start)]

// CHECK-LABEL: @main
// CHECK: load volatile i8, {{.+}} @__rustc_debug_gdb_scripts_section__

#[start]
fn start(_: isize, _: *const *const u8) -> isize {
    return 0;
}


