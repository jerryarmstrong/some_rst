tests/ui/regions/regions-dependent-autofn.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test lifetimes are linked properly when we autoslice a vector.
// Issue #3148.

// pretty-expanded FIXME #23616

fn subslice<F>(v: F) -> F where F: FnOnce() { v }

fn both<F>(v: F) -> F where F: FnOnce() {
    subslice(subslice(v))
}

pub fn main() {
    both(main);
}


