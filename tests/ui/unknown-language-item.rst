tests/ui/unknown-language-item.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused)]
#![feature(lang_items)]

#[lang = "foo"]
fn bar() -> ! {
//~^^ ERROR definition of an unknown language item: `foo`
    loop {}
}

fn main() {}


