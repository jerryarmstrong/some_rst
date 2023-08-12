tests/ui/issues/issue-49851/compiler-builtins-error.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //~ ERROR can't find crate for `core`
//~^ ERROR can't find crate for `compiler_builtins`

// compile-flags: --target thumbv7em-none-eabihf
// needs-llvm-components: arm
#![deny(unsafe_code)]
#![deny(warnings)]
#![no_std]

extern crate cortex_m;
//~^ ERROR can't find crate for `cortex_m`

fn main() {}


