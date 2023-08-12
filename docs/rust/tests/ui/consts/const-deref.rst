tests/ui/consts/const-deref.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

const C: &'static isize = &1000;
static D: isize = *C;

pub fn main() {
    assert_eq!(D, 1000);
}


