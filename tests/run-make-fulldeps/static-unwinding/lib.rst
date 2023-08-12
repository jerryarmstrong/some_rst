tests/run-make-fulldeps/static-unwinding/lib.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]

pub static mut statik: isize = 0;

struct A;
impl Drop for A {
    fn drop(&mut self) {
        unsafe { statik = 1; }
    }
}

pub fn callback<F>(f: F) where F: FnOnce() {
    let _a = A;
    f();
}


