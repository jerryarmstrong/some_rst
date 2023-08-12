crates/core_arch/src/acle/registers/v7m.rs
==========================================

Last edited: 2019-05-15 21:04:28

Contents:

.. code-block:: rs

    /// Base Priority Mask Register
pub struct BASEPRI;

rsr!(BASEPRI);
wsr!(BASEPRI);

/// Base Priority Mask Register (conditional write)
#[allow(non_camel_case_types)]
pub struct BASEPRI_MAX;

wsr!(BASEPRI_MAX);

/// Fault Mask Register
pub struct FAULTMASK;

rsr!(FAULTMASK);
wsr!(FAULTMASK);


