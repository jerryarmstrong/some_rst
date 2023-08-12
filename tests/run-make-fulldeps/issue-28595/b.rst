tests/run-make-fulldeps/issue-28595/b.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate a;

#[link(name = "b", kind = "static")]
extern "C" {
    pub fn b();
}

fn main() {
    unsafe {
        b();
    }
}


