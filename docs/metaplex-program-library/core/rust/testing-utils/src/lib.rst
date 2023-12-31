core/rust/testing-utils/src/lib.rs
==================================

Last edited: 2023-07-31 23:00:16

Contents:

.. code-block:: rs

    pub mod solana;
pub mod utils;

#[macro_export]
macro_rules! assert_transport_error {
    ($error:expr, $matcher:pat) => {
        match $error {
            $matcher => {
                assert!(true)
            }
            _ => assert!(false),
        }
    };
}

#[macro_export]
macro_rules! assert_error {
    ($error:expr, $matcher:expr) => {
        match $error {
            BanksClientError::TransactionError(TransactionError::InstructionError(
                0,
                InstructionError::Custom(x),
            )) => assert_eq!(x, $matcher),
            _ => assert!(false),
        };
    };
}

#[macro_export]
macro_rules! assert_custom_error {
    ($error:expr, $matcher:pat) => {
        match $error {
            BanksClientError::TransactionError(TransactionError::InstructionError(
                0,
                InstructionError::Custom(x),
            )) => match FromPrimitive::from_i32(x as i32) {
                Some($matcher) => assert!(true),
                _ => assert!(false),
            },
            _ => assert!(false),
        };
    };
}


