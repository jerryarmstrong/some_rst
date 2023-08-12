tests/ui/feature-gates/feature-gate-abi_ptx.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // needs-llvm-components: nvptx
// compile-flags: --target=nvptx64-nvidia-cuda --crate-type=rlib
#![no_core]
#![feature(no_core, lang_items)]
#[lang="sized"]
trait Sized { }

extern "ptx-kernel" fn fu() {} //~ ERROR PTX ABIs are experimental

trait T {
    extern "ptx-kernel" fn mu(); //~ ERROR PTX ABIs are experimental
    extern "ptx-kernel" fn dmu() {} //~ ERROR PTX ABIs are experimental
}

struct S;
impl T for S {
    extern "ptx-kernel" fn mu() {} //~ ERROR PTX ABIs are experimental
}

impl S {
    extern "ptx-kernel" fn imu() {} //~ ERROR PTX ABIs are experimental
}

type TAU = extern "ptx-kernel" fn(); //~ ERROR PTX ABIs are experimental

extern "ptx-kernel" {} //~ ERROR PTX ABIs are experimental


