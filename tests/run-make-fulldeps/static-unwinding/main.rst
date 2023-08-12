tests/run-make-fulldeps/static-unwinding/main.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate lib;

use std::thread;

static mut statik: isize = 0;

struct A;
impl Drop for A {
    fn drop(&mut self) {
        unsafe { statik = 1; }
    }
}

fn main() {
    thread::spawn(move|| {
        let _a = A;
        lib::callback(|| panic!());
    }).join().unwrap_err();

    unsafe {
        assert_eq!(lib::statik, 1);
        assert_eq!(statik, 1);
    }
}


