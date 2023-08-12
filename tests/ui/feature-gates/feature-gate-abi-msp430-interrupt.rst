tests/ui/feature-gates/feature-gate-abi-msp430-interrupt.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // needs-llvm-components: msp430
// compile-flags: --target=msp430-none-elf --crate-type=rlib
#![no_core]
#![feature(no_core, lang_items)]
#[lang="sized"]
trait Sized { }

extern "msp430-interrupt" fn f() {}
//~^ ERROR msp430-interrupt ABI is experimental

trait T {
    extern "msp430-interrupt" fn m();
    //~^ ERROR msp430-interrupt ABI is experimental

    extern "msp430-interrupt" fn dm() {}
    //~^ ERROR msp430-interrupt ABI is experimental
}

struct S;
impl T for S {
    extern "msp430-interrupt" fn m() {}
    //~^ ERROR msp430-interrupt ABI is experimental
}

impl S {
    extern "msp430-interrupt" fn im() {}
    //~^ ERROR msp430-interrupt ABI is experimental
}

type TA = extern "msp430-interrupt" fn();
//~^ ERROR msp430-interrupt ABI is experimental

extern "msp430-interrupt" {}
//~^ ERROR msp430-interrupt ABI is experimental


