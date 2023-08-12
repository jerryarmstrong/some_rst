tests/ui/deref-rc.rs
====================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use std::rc::Rc;

fn main() {
    let x = Rc::new([1, 2, 3, 4]);
    assert_eq!(*x, [1, 2, 3, 4]);
}


