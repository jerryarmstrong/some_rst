tests/codegen/mainsubprogram.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test depends on a patch that was committed to upstream LLVM
// before 4.0, formerly backported to the Rust LLVM fork.

// ignore-windows
// ignore-macos

// compile-flags: -g -C no-prepopulate-passes

// CHECK-LABEL: @main
// CHECK: {{.*}}DISubprogram{{.*}}name: "main",{{.*}}DI{{(SP)?}}FlagMainSubprogram{{.*}}

pub fn main() {
}


