tests/ui/empty-allocation-rvalue-non-null.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(unused_variables)]
// pretty-expanded FIXME #23616

pub fn main() {
    let x = *Box::new(());
}


