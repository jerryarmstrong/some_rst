src/tools/clippy/tests/ui/zero_ptr.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
pub fn foo(_const: *const f32, _mut: *mut i64) {}

fn main() {
    let _ = 0 as *const usize;
    let _ = 0 as *mut f64;
    let _: *const u8 = 0 as *const _;

    foo(0 as _, 0 as _);
    foo(0 as *const _, 0 as *mut _);

    let z = 0;
    let _ = z as *const usize; // this is currently not caught
}


