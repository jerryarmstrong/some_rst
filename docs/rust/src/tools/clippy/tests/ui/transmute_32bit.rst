src/tools/clippy/tests/ui/transmute_32bit.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-64bit

#[warn(clippy::wrong_transmute)]
fn main() {
    unsafe {
        let _: *const usize = std::mem::transmute(6.0f32);

        let _: *mut usize = std::mem::transmute(6.0f32);

        let _: *const usize = std::mem::transmute('x');

        let _: *mut usize = std::mem::transmute('x');
    }
}


