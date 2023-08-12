tests/ui/transmute/transmute-imut-to-mut.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that transmuting from &T to &mut T is Undefined Behavior.

use std::mem::transmute;

fn main() {
    let _a: &mut u8 = unsafe { transmute(&1u8) };
    //~^ ERROR transmuting &T to &mut T is undefined behavior, even if the reference is unused, consider instead using an UnsafeCell
}


