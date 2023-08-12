tests/run-make-fulldeps/pointer-auth-link-with-c/test.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[link(name = "test")]
extern "C" {
    fn foo() -> i32;
}

fn main() {
    unsafe {foo();}
}


