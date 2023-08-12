programs/sbf/rust/invoke/src/instructions.rs
============================================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    //! Example Rust-based SBF program that issues a cross-program-invocation

pub const TEST_SUCCESS: u8 = 1;
pub const TEST_PRIVILEGE_ESCALATION_SIGNER: u8 = 2;
pub const TEST_PRIVILEGE_ESCALATION_WRITABLE: u8 = 3;
pub const TEST_PPROGRAM_NOT_EXECUTABLE: u8 = 4;
pub const TEST_EMPTY_ACCOUNTS_SLICE: u8 = 5;
pub const TEST_CAP_SEEDS: u8 = 6;
pub const TEST_CAP_SIGNERS: u8 = 7;
pub const TEST_ALLOC_ACCESS_VIOLATION: u8 = 8;
pub const TEST_MAX_INSTRUCTION_DATA_LEN_EXCEEDED: u8 = 9;
pub const TEST_MAX_INSTRUCTION_ACCOUNTS_EXCEEDED: u8 = 10;
pub const TEST_RETURN_ERROR: u8 = 11;
pub const TEST_PRIVILEGE_DEESCALATION_ESCALATION_SIGNER: u8 = 12;
pub const TEST_PRIVILEGE_DEESCALATION_ESCALATION_WRITABLE: u8 = 13;
pub const TEST_WRITABLE_DEESCALATION_WRITABLE: u8 = 14;
pub const TEST_NESTED_INVOKE_TOO_DEEP: u8 = 15;
pub const TEST_CALL_PRECOMPILE: u8 = 16;
pub const ADD_LAMPORTS: u8 = 17;
pub const TEST_RETURN_DATA_TOO_LARGE: u8 = 18;
pub const TEST_DUPLICATE_PRIVILEGE_ESCALATION_SIGNER: u8 = 19;
pub const TEST_DUPLICATE_PRIVILEGE_ESCALATION_WRITABLE: u8 = 20;
pub const TEST_MAX_ACCOUNT_INFOS_EXCEEDED: u8 = 21;

pub const MINT_INDEX: usize = 0;
pub const ARGUMENT_INDEX: usize = 1;
pub const INVOKED_PROGRAM_INDEX: usize = 2;
pub const INVOKED_ARGUMENT_INDEX: usize = 3;
pub const INVOKED_PROGRAM_DUP_INDEX: usize = 4;
pub const ARGUMENT_DUP_INDEX: usize = 5;
pub const DERIVED_KEY1_INDEX: usize = 6;
pub const DERIVED_KEY2_INDEX: usize = 7;
pub const DERIVED_KEY3_INDEX: usize = 8;
pub const SYSTEM_PROGRAM_INDEX: usize = 9;
pub const FROM_INDEX: usize = 10;
pub const ED25519_PROGRAM_INDEX: usize = 11;
pub const INVOKE_PROGRAM_INDEX: usize = 12;


