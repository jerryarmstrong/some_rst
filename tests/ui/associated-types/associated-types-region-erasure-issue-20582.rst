tests/ui/associated-types/associated-types-region-erasure-issue-20582.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// Regression test for #20582. This test caused an ICE related to
// inconsistent region erasure in codegen.

// pretty-expanded FIXME #23616

struct Foo<'a> {
    buf: &'a[u8]
}

impl<'a> Iterator for Foo<'a> {
    type Item = &'a[u8];

    fn next(&mut self) -> Option<<Self as Iterator>::Item> {
        Some(self.buf)
    }
}

fn main() {
}


