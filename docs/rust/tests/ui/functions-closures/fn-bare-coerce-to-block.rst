tests/ui/functions-closures/fn-bare-coerce-to-block.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

fn bare() {}

fn likes_block<F>(f: F) where F: FnOnce() { f() }

pub fn main() {
    likes_block(bare);
}


