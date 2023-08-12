tests/ui/deref.rs
=================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

pub fn main() {
    let x: Box<isize> = Box::new(10);
    let _y: isize = *x;
}


