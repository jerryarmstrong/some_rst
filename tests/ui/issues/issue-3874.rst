tests/ui/issues/issue-3874.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

enum PureCounter { PureCounterVariant(usize) }

fn each<F>(thing: PureCounter, blk: F) where F: FnOnce(&usize) {
    let PureCounter::PureCounterVariant(ref x) = thing;
    blk(x);
}

pub fn main() {}


