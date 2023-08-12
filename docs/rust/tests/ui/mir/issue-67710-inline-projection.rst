tests/ui/mir/issue-67710-inline-projection.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z mir-opt-level=3
// build-pass

// This used to ICE due to the inling pass not examining projections
// for references to locals

pub fn parse(version: ()) {
    p(&b'.', b"0");
}
#[inline(always)]
fn p(byte: &u8, s: &[u8]) {
    !(s[0] == *byte);
}

fn main() {
    parse(());
}


