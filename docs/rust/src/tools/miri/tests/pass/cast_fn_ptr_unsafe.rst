src/tools/miri/tests/pass/cast_fn_ptr_unsafe.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    fn f() {}

    let g = f as fn() as unsafe fn();
    unsafe {
        g();
    }
}


