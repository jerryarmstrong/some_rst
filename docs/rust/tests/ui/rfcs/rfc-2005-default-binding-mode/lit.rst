tests/ui/rfcs/rfc-2005-default-binding-mode/lit.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
fn with_u8() {
    let s = 5u8;
    let r = match &s {
        4 => false,
        5 => true,
        _ => false,
    };
    assert!(r);
}

// A string literal isn't mistaken for a non-ref pattern (in which case we'd
// deref `s` and mess things up).
fn with_str() {
    let s: &'static str = "abc";
    match s {
            "abc" => true,
            _ => panic!(),
    };
}

// Ditto with byte strings.
fn with_bytes() {
    let s: &'static [u8] = b"abc";
    match s {
        b"abc" => true,
        _ => panic!(),
    };
}

pub fn main() {
    with_str();
}


