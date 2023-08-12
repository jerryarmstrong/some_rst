tests/ui/pin-macro/cant_access_internals.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

use core::{
    marker::PhantomPinned,
    mem,
    pin::{pin, Pin},
};

fn main() {
    let mut phantom_pinned = pin!(PhantomPinned);
    mem::take(phantom_pinned.pointer); //~ ERROR use of unstable library feature 'unsafe_pin_internals'
}


