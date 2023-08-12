tests/ui/unsafe-pointer-assignability.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn f(x: *const isize) {
    unsafe {
        assert_eq!(*x, 3);
    }
}

pub fn main() {
    f(&3);
}


