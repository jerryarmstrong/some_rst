src/tools/rustfmt/tests/target/cfg_if/mod.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! `std_detect`

#[doc(hidden)] // unstable implementation detail
#[unstable(feature = "stdsimd", issue = "27731")]
pub mod detect;


