crates/std_detect/src/mod.rs
============================

Last edited: 2019-05-15 21:04:28

Contents:

.. code-block:: rs

    //! `std_detect`

#[doc(hidden)] // unstable implementation detail
#[unstable(feature = "stdsimd", issue = "27731")]
pub mod detect;


