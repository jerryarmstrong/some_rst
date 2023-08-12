tests/run-make/raw-dylib-inline-cross-dylib/lib_wrapper.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate raw_dylib_test;

#[inline]
pub fn inline_library_function_calls_inline() {
    raw_dylib_test::inline_library_function();
}


