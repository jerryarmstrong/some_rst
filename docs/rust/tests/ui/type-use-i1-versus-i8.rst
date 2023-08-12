tests/ui/type-use-i1-versus-i8.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

use std::ptr;

pub fn main() {
    unsafe {
        let mut x: bool = false;
        // this line breaks it
        ptr::write(&mut x, false);
    }
}


