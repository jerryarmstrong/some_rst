crates/core_arch/src/x86_64/sse42.rs
====================================

Last edited: 2019-05-15 21:04:28

Contents:

.. code-block:: rs

    //! `x86_64`'s Streaming SIMD Extensions 4.2 (SSE4.2)

#[cfg(test)]
use stdsimd_test::assert_instr;

#[allow(improper_ctypes)]
extern "C" {
    #[link_name = "llvm.x86.sse42.crc32.64.64"]
    fn crc32_64_64(crc: u64, v: u64) -> u64;
}

/// Starting with the initial value in `crc`, return the accumulated
/// CRC32 value for unsigned 64-bit integer `v`.
///
/// [Intel's documentation](https://software.intel.com/sites/landingpage/IntrinsicsGuide/#text=_mm_crc32_u64)
#[inline]
#[target_feature(enable = "sse4.2")]
#[cfg_attr(test, assert_instr(crc32))]
#[stable(feature = "simd_x86", since = "1.27.0")]
pub unsafe fn _mm_crc32_u64(crc: u64, v: u64) -> u64 {
    crc32_64_64(crc, v)
}

#[cfg(test)]
mod tests {
    use crate::core_arch::arch::x86_64::*;

    use stdsimd_test::simd_test;

    #[simd_test(enable = "sse4.2")]
    unsafe fn test_mm_crc32_u64() {
        let crc = 0x7819dccd3e824;
        let v = 0x2a22b845fed;
        let i = _mm_crc32_u64(crc, v);
        assert_eq!(i, 0xbb6cdc6c);
    }
}


