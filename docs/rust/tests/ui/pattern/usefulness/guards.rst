tests/ui/pattern/usefulness/guards.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(exclusive_range_pattern)]
#![deny(unreachable_patterns)]

enum Q { R(Option<usize>) }

pub fn main() {
    match Q::R(None) {
        Q::R(S) if S.is_some() => {}
        _ => {}
    }

    match 0u8 { //~ ERROR non-exhaustive patterns
        0 .. 128 => {}
        128 ..= 255 if true => {}
    }

    match 0u8 {
        0 .. 128 => {}
        128 ..= 255 if false => {}
        128 ..= 255 => {} // ok, because previous arm was guarded
    }
}


