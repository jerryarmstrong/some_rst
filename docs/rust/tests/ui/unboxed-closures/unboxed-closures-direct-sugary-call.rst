tests/ui/unboxed-closures/unboxed-closures-direct-sugary-call.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_mut)]
// pretty-expanded FIXME #23616

fn main() {
    let mut unboxed = || {};
    unboxed();
}


