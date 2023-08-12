tests/ui/lifetimes/fullwidth-ampersand.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Verify that we do not ICE when the user uses a multubyte ampersand.

fn f(_: &＆()) -> &() { todo!() }
//~^ ERROR unknown start of token: \u{ff06}
//~| ERROR missing lifetime specifier [E0106]

fn main() {}


