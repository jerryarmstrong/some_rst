tests/rustdoc/force-target-feature.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // only-x86_64
// compile-flags:--test -C target-feature=+avx
// should-fail

/// (written on a spider's web) Some Struct
///
/// ```
/// panic!("oh no");
/// ```
#[doc(cfg(target_feature = "avx"))]
pub struct SomeStruct;


