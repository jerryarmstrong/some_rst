crates/core_arch/src/x86_64/bswap.rs
====================================

Last edited: 2019-05-15 21:04:28

Contents:

.. code-block:: rs

    //! Byte swap intrinsics.

#![allow(clippy::module_name_repetitions)]

#[cfg(test)]
use stdsimd_test::assert_instr;

/// Returns an integer with the reversed byte order of x
///
/// [Intel's documentation](https://software.intel.com/sites/landingpage/IntrinsicsGuide/#text=_bswap64)
#[inline]
#[cfg_attr(test, assert_instr(bswap))]
#[stable(feature = "simd_x86", since = "1.27.0")]
pub unsafe fn _bswap64(x: i64) -> i64 {
    bswap_i64(x)
}

#[allow(improper_ctypes)]
extern "C" {
    #[link_name = "llvm.bswap.i64"]
    fn bswap_i64(x: i64) -> i64;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_bswap64() {
        unsafe {
            assert_eq!(_bswap64(0x0EADBEEFFADECA0E), 0x0ECADEFAEFBEAD0E);
            assert_eq!(_bswap64(0x0000000000000000), 0x0000000000000000);
        }
    }
}


