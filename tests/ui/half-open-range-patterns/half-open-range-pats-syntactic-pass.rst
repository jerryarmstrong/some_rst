tests/ui/half-open-range-patterns/half-open-range-pats-syntactic-pass.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// Test the parsing of half-open ranges.

#![feature(exclusive_range_pattern)]

fn main() {}

#[cfg(FALSE)]
fn syntax() {
    match scrutinee {
        X.. | 0.. | 'a'.. | 0.0f32.. => {}
        ..=X | ..X => {}
        ..=0 | ..0 => {}
        ..='a' | ..'a' => {}
        ..=0.0f32 | ..0.0f32 => {}
    }
}

fn syntax2() {
    macro_rules! mac {
        ($e:expr) => {
            match 0u8 { ..$e => {}, _ => {} }
            match 0u8 { ..=$e => {}, _ => {} }
            match 0u8 { $e.. => {}, _ => {} }
        }
    }
    mac!(42u8);
}


