tests/ui/cmse-nonsecure/cmse-nonsecure-entry/wrong-abi.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --target thumbv8m.main-none-eabi --crate-type lib
// needs-llvm-components: arm
#![feature(cmse_nonsecure_entry, no_core, lang_items)]
#![no_core]
#[lang="sized"]
trait Sized { }

#[no_mangle]
#[cmse_nonsecure_entry]
//~^ ERROR `#[cmse_nonsecure_entry]` requires C ABI [E0776]
pub fn entry_function(_: u32, _: u32, _: u32, d: u32) -> u32 {
    d
}


