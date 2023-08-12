src/tools/rustfmt/tests/source/issue_4528.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(clippy::no_effect)]
 
extern "C" {
 // N.B., mutability can be easily incorrect in FFI calls -- as
     // in C, the default is mutable pointers.
    fn ffi(c: *mut u8);
     fn int_ffi(c: *mut i32);
}

