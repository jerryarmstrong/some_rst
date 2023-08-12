src/tools/clippy/tests/ui/crashes/ice_exacte_size.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(clippy::all)]

/// Test for https://github.com/rust-lang/rust-clippy/issues/1336

#[allow(dead_code)]
struct Foo;

impl Iterator for Foo {
    type Item = ();

    fn next(&mut self) -> Option<()> {
        let _ = self.len() == 0;
        unimplemented!()
    }
}

impl ExactSizeIterator for Foo {}

fn main() {}


