src/tools/rustfmt/tests/source/cfg_if/detect/os/freebsd/powerpc.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Run-time feature detection for PowerPC on FreeBSD.

use crate::detect::{Feature, cache};
use super::{auxvec};

/// Performs run-time feature detection.
#[inline]
pub fn check_for(x: Feature) -> bool {
    cache::test(x as u32, detect_features)
}

fn detect_features() -> cache::Initializer {
    let mut value = cache::Initializer::default();
    let enable_feature = |value: &mut cache::Initializer, f, enable| {
        if enable {
            value.set(f as u32);
        }
    };

    if let Ok(auxv) = auxvec::auxv() {
        enable_feature(&mut value, Feature::altivec, auxv.hwcap & 0x10000000 != 0);
        enable_feature(&mut value, Feature::vsx, auxv.hwcap & 0x00000080 != 0);
        enable_feature(&mut value, Feature::power8, auxv.hwcap2 & 0x80000000 != 0);
        return value;
    }
    value
}


