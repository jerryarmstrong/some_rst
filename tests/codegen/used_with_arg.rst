tests/codegen/used_with_arg.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]
#![feature(used_with_arg)]

// CHECK: @llvm.used = appending global {{.*}}USED_LINKER
#[used(linker)]
static mut USED_LINKER: [usize; 1] = [0];

// CHECK-NEXT: @llvm.compiler.used = appending global {{.*}}USED_COMPILER
#[used(compiler)]
static mut USED_COMPILER: [usize; 1] = [0];


