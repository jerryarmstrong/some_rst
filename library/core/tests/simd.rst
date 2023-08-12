library/core/tests/simd.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use core::simd::f32x4;
use core::simd::SimdFloat;

#[test]
fn testing() {
    let x = f32x4::from_array([1.0, 1.0, 1.0, 1.0]);
    let y = -x;

    let h = x * f32x4::splat(0.5);

    let r = y.abs();
    assert_eq!(x, r);
    assert_eq!(h, f32x4::splat(0.5));
}


