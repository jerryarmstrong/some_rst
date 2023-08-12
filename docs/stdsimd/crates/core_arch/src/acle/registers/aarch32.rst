crates/core_arch/src/acle/registers/aarch32.rs
==============================================

Last edited: 2019-05-15 21:04:28

Contents:

.. code-block:: rs

    /// Application Program Status Register
pub struct APSR;

// Note (@Lokathor): Because this breaks the use of Rust on the Game Boy
// Advance, this change must be reverted until Rust learns to handle cpu state
// properly. See also: https://github.com/rust-lang-nursery/stdsimd/issues/702

//#[cfg(any(not(target_feature = "thumb-state"), target_feature = "v6t2"))]
//rsr!(APSR);


