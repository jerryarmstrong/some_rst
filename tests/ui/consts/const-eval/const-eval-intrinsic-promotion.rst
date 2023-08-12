tests/ui/consts/const-eval/const-eval-intrinsic-promotion.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(core_intrinsics)]
fn main() {
    // Test that calls to intrinsics are never promoted
    let x: &'static usize =
        &std::intrinsics::size_of::<i32>(); //~ ERROR temporary value dropped while borrowed
}


