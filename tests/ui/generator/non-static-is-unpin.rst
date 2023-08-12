tests/ui/generator/non-static-is-unpin.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(generators, generator_trait)]

use std::marker::{PhantomPinned, Unpin};

fn assert_unpin<G: Unpin>(_: G) {
}

fn main() {
    // Even though this generator holds a `PhantomPinned` in its environment, it
    // remains `Unpin`.
    assert_unpin(|| {
        let pinned = PhantomPinned;
        yield;
        drop(pinned);
    });
}


