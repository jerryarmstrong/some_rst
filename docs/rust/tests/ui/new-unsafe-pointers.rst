tests/ui/new-unsafe-pointers.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

fn main() {
    let _a: *const isize = 3 as *const isize;
    let _a: *mut isize = 3 as *mut isize;
}


