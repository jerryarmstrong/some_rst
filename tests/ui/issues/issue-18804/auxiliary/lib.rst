tests/ui/issues/issue-18804/auxiliary/lib.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]
#![feature(linkage)]

pub fn foo<T>() -> *const () {
    extern "C" {
        #[linkage = "extern_weak"]
        static FOO: *const ();
    }
    unsafe { FOO }
}


