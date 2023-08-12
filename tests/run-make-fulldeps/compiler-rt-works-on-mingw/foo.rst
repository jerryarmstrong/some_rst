tests/run-make-fulldeps/compiler-rt-works-on-mingw/foo.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "C" {
    fn foo();
}

pub fn main() {
    unsafe {
        foo();
    }
    assert_eq!(7f32.powi(3), 343f32);
}


