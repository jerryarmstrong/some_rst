tests/ui/conditional-compilation/cfg-attr-multi-false.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that cfg_attr doesn't emit any attributes when the
// configuration variable is false. This mirrors `cfg-attr-multi-true.rs`

// build-pass (FIXME(62277): could be check-pass?)

#![warn(unused_must_use)]

#[cfg_attr(any(), deprecated, must_use)]
struct Struct {}

impl Struct {
    fn new() -> Struct {
        Struct {}
    }
}

fn main() {
    Struct::new();
}


