tests/ui/lang-items/no_owned_box_lang_item.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we don't ICE when we are missing the owned_box lang item.

// error-pattern: requires `owned_box` lang_item

#![feature(lang_items, box_syntax)]
#![no_std]

use core::panic::PanicInfo;

fn main() {
    let x = box 1i32;
}

#[lang = "eh_personality"] extern "C" fn eh_personality() {}
#[lang = "eh_catch_typeinfo"] static EH_CATCH_TYPEINFO: u8 = 0;
#[lang = "panic_impl"] fn panic_impl(panic: &PanicInfo) -> ! { loop {} }


