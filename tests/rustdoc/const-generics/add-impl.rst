tests/rustdoc/const-generics/add-impl.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

use std::ops::Add;

// @has foo/struct.Simd.html '//div[@class="item-decl"]/pre[@class="rust"]' 'pub struct Simd<T, const WIDTH: usize>'
pub struct Simd<T, const WIDTH: usize> {
    inner: T,
}

// @has foo/struct.Simd.html '//div[@id="trait-implementations-list"]//h3[@class="code-header"]' 'impl Add<Simd<u8, 16>> for Simd<u8, 16>'
impl Add for Simd<u8, 16> {
    type Output = Self;

    fn add(self, rhs: Self) -> Self::Output {
        Self { inner: 0 }
    }
}


