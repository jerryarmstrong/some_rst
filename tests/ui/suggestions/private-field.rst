tests/ui/suggestions/private-field.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --crate-type lib
pub struct S {
    pub val: string::MyString,
}

pub fn test(s: S) {
    dbg!(s.cap) //~ ERROR: no field `cap` on type `S` [E0609]
}

pub(crate) mod string {

    pub struct MyString {
        buf: MyVec,
    }

    struct MyVec {
        cap: usize,
    }
}


