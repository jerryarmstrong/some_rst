library/portable-simd/crates/core_simd/src/elements/uint.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use super::sealed::Sealed;
use crate::simd::{intrinsics, LaneCount, Simd, SupportedLaneCount};

/// Operations on SIMD vectors of unsigned integers.
pub trait SimdUint: Copy + Sealed {
    /// Scalar type contained by this SIMD vector type.
    type Scalar;

    /// Lanewise saturating add.
    ///
    /// # Examples
    /// ```
    /// # #![feature(portable_simd)]
    /// # #[cfg(feature = "as_crate")] use core_simd::simd;
    /// # #[cfg(not(feature = "as_crate"))] use core::simd;
    /// # use simd::{Simd, SimdUint};
    /// use core::u32::MAX;
    /// let x = Simd::from_array([2, 1, 0, MAX]);
    /// let max = Simd::splat(MAX);
    /// let unsat = x + max;
    /// let sat = x.saturating_add(max);
    /// assert_eq!(unsat, Simd::from_array([1, 0, MAX, MAX - 1]));
    /// assert_eq!(sat, max);
    /// ```
    fn saturating_add(self, second: Self) -> Self;

    /// Lanewise saturating subtract.
    ///
    /// # Examples
    /// ```
    /// # #![feature(portable_simd)]
    /// # #[cfg(feature = "as_crate")] use core_simd::simd;
    /// # #[cfg(not(feature = "as_crate"))] use core::simd;
    /// # use simd::{Simd, SimdUint};
    /// use core::u32::MAX;
    /// let x = Simd::from_array([2, 1, 0, MAX]);
    /// let max = Simd::splat(MAX);
    /// let unsat = x - max;
    /// let sat = x.saturating_sub(max);
    /// assert_eq!(unsat, Simd::from_array([3, 2, 1, 0]));
    /// assert_eq!(sat, Simd::splat(0));
    fn saturating_sub(self, second: Self) -> Self;

    /// Returns the sum of the lanes of the vector, with wrapping addition.
    fn reduce_sum(self) -> Self::Scalar;

    /// Returns the product of the lanes of the vector, with wrapping multiplication.
    fn reduce_product(self) -> Self::Scalar;

    /// Returns the maximum lane in the vector.
    fn reduce_max(self) -> Self::Scalar;

    /// Returns the minimum lane in the vector.
    fn reduce_min(self) -> Self::Scalar;

    /// Returns the cumulative bitwise "and" across the lanes of the vector.
    fn reduce_and(self) -> Self::Scalar;

    /// Returns the cumulative bitwise "or" across the lanes of the vector.
    fn reduce_or(self) -> Self::Scalar;

    /// Returns the cumulative bitwise "xor" across the lanes of the vector.
    fn reduce_xor(self) -> Self::Scalar;
}

macro_rules! impl_trait {
    { $($ty:ty),* } => {
        $(
        impl<const LANES: usize> Sealed for Simd<$ty, LANES>
        where
            LaneCount<LANES>: SupportedLaneCount,
        {
        }

        impl<const LANES: usize> SimdUint for Simd<$ty, LANES>
        where
            LaneCount<LANES>: SupportedLaneCount,
        {
            type Scalar = $ty;

            #[inline]
            fn saturating_add(self, second: Self) -> Self {
                // Safety: `self` is a vector
                unsafe { intrinsics::simd_saturating_add(self, second) }
            }

            #[inline]
            fn saturating_sub(self, second: Self) -> Self {
                // Safety: `self` is a vector
                unsafe { intrinsics::simd_saturating_sub(self, second) }
            }

            #[inline]
            fn reduce_sum(self) -> Self::Scalar {
                // Safety: `self` is an integer vector
                unsafe { intrinsics::simd_reduce_add_ordered(self, 0) }
            }

            #[inline]
            fn reduce_product(self) -> Self::Scalar {
                // Safety: `self` is an integer vector
                unsafe { intrinsics::simd_reduce_mul_ordered(self, 1) }
            }

            #[inline]
            fn reduce_max(self) -> Self::Scalar {
                // Safety: `self` is an integer vector
                unsafe { intrinsics::simd_reduce_max(self) }
            }

            #[inline]
            fn reduce_min(self) -> Self::Scalar {
                // Safety: `self` is an integer vector
                unsafe { intrinsics::simd_reduce_min(self) }
            }

            #[inline]
            fn reduce_and(self) -> Self::Scalar {
                // Safety: `self` is an integer vector
                unsafe { intrinsics::simd_reduce_and(self) }
            }

            #[inline]
            fn reduce_or(self) -> Self::Scalar {
                // Safety: `self` is an integer vector
                unsafe { intrinsics::simd_reduce_or(self) }
            }

            #[inline]
            fn reduce_xor(self) -> Self::Scalar {
                // Safety: `self` is an integer vector
                unsafe { intrinsics::simd_reduce_xor(self) }
            }
        }
        )*
    }
}

impl_trait! { u8, u16, u32, u64, usize }


