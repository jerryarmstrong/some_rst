tests/ui/rust-2018/macro-use-warned-against.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:macro-use-warned-against.rs
// aux-build:macro-use-warned-against2.rs
// check-pass

#![warn(macro_use_extern_crate, unused)]

#[macro_use] //~ WARN should be replaced at use sites with a `use` item
extern crate macro_use_warned_against;
#[macro_use] //~ WARN unused `#[macro_use]`
extern crate macro_use_warned_against2;

fn main() {
    foo!();
}


