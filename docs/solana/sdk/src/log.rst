sdk/src/log.rs
==============

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    #![cfg(feature = "program")]

pub use solana_program::log::*;

#[macro_export]
#[deprecated(
    since = "1.4.3",
    note = "Please use `solana_program::log::info` instead"
)]
macro_rules! info {
    ($msg:expr) => {
        $crate::log::sol_log($msg)
    };
}


