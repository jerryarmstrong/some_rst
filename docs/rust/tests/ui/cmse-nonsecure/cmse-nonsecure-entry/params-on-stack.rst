tests/ui/cmse-nonsecure/cmse-nonsecure-entry/params-on-stack.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail
// compile-flags: --target thumbv8m.main-none-eabi --crate-type lib
// needs-llvm-components: arm
#![feature(cmse_nonsecure_entry, no_core, lang_items)]
#![no_core]
#[lang="sized"]
trait Sized { }
#[lang="copy"]
trait Copy { }
impl Copy for u32 {}

#[no_mangle]
#[cmse_nonsecure_entry]
pub extern "C" fn entry_function(_: u32, _: u32, _: u32, _: u32, e: u32) -> u32 {
    e
}


