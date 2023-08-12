tests/ui/array-slice-vec/vector-no-ann-2.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// pretty-expanded FIXME #23616

pub fn main() {
    let _quux: Box<Vec<usize>> = Box::new(Vec::new());
}


