tests/ui/proc-macro/meta-delim.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:meta-delim.rs
// edition:2018
// run-pass

// Tests that we can properly deserialize a macro with strange delimiters
// See https://github.com/rust-lang/rust/pull/73569#issuecomment-650860457

extern crate meta_delim;

fn main() {
    assert_eq!("a bunch of idents", meta_delim::meta_delim!(a bunch of idents));
}


