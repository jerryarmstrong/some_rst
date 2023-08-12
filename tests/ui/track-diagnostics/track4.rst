tests/ui/track-diagnostics/track4.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z track-diagnostics
// error-pattern: created at

// Normalize the emitted location so this doesn't need
// updating everytime someone adds or removes a line.
// normalize-stderr-test ".rs:\d+:\d+" -> ".rs:LL:CC"

pub onion {
    Owo(u8),
    Uwu(i8),
}

fn main() {}


