tests/ui/unique/unique-create.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

pub fn main() {
    let _: Box<_> = Box::new(100);
}

fn vec() {
    vec![0];
}


