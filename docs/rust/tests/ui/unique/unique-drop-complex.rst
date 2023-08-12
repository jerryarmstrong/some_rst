tests/ui/unique/unique-drop-complex.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

pub fn main() {
    let _x: Box<_> = Box::new(vec![0,0,0,0,0]);
}


