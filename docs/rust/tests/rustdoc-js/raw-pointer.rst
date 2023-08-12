tests/rustdoc-js/raw-pointer.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::ptr;

pub struct Aaaaaaa {}

pub fn bbbbbbb() -> *const Aaaaaaa {
    ptr::null()
}

pub struct Ccccccc {}

impl Ccccccc {
    pub fn ddddddd(&self) -> *const Aaaaaaa {
        ptr::null()
    }
    pub fn eeeeeee(&self, _x: *const Aaaaaaa) -> i32 {
        0
    }
    pub fn fffffff(&self, x: *const Aaaaaaa) -> *const Aaaaaaa {
        x
    }
    pub fn ggggggg(&self, x: *mut Aaaaaaa) -> *mut Aaaaaaa {
        x
    }
}


