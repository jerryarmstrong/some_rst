tests/run-make-fulldeps/link-path-order/main.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustc_private)]

extern crate libc;

#[link(name = "foo", kind = "static")]
extern "C" {
    fn should_return_one() -> libc::c_int;
}

fn main() {
    let result = unsafe { should_return_one() };

    if result != 1 {
        std::process::exit(255);
    }
}


