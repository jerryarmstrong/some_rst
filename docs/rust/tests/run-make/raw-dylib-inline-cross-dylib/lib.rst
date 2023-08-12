tests/run-make/raw-dylib-inline-cross-dylib/lib.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(raw_dylib)]

#[link(name = "extern_1", kind = "raw-dylib")]
extern {
    fn extern_fn_1();
    fn extern_fn_2();
}

#[inline]
pub fn inline_library_function() {
    unsafe {
        extern_fn_1();
        extern_fn_2();
    }
}

pub fn library_function() {
    unsafe {
        extern_fn_2();
    }
}


