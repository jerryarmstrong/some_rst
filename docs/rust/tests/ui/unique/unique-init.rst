tests/ui/unique/unique-init.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

pub fn main() {
    let _i: Box<_> = Box::new(100);
}


