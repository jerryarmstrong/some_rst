tests/ui/cmse-nonsecure/cmse-nonsecure-call/wrong-abi-location-2.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --target thumbv8m.main-none-eabi --crate-type lib
// needs-llvm-components: arm
#![feature(abi_c_cmse_nonsecure_call, lang_items, no_core)]
#![no_core]
#[lang="sized"]
trait Sized { }

extern "C-cmse-nonsecure-call" { //~ ERROR [E0781]
    fn test();
}


