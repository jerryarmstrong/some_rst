tests/ui/cross-crate/auxiliary/xcrate_address_insignificant.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn foo<T>() -> isize {
    static a: isize = 3;
    a
}

pub fn bar() -> isize {
    foo::<isize>()
}


