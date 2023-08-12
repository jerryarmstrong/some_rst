tests/ui/stable-addr-of.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Issue #2040


pub fn main() {
    let foo: isize = 1;
    assert_eq!(&foo as *const isize, &foo as *const isize);
}


