tests/ui/rfc-2091-track-caller/macro-declaration.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// See https://github.com/rust-lang/rust/issues/95151
#[track_caller]
macro_rules! _foo {
    () => {};
}

fn main() {
}


