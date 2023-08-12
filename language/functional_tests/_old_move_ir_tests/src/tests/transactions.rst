language/functional_tests/_old_move_ir_tests/src/tests/transactions.rs
======================================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use crate::*;
use move_ir::{assert_error_type, assert_no_error};
use proptest::prelude::*;
use solana_libra_types::{
    account_address::AccountAddress,
    transaction::{TransactionArgument, TransactionPayload},
};

#[test]
fn write_set_txn_roundtrip() {
    // Creating a new test environment is expensive so do it outside the proptest environment.
    let test_env = TestEnvironment::default();

    proptest!(|(signed_txn in SignedTransaction::genesis_strategy())| {
        let write_set = match signed_txn.payload() {
            TransactionPayload::WriteSet(write_set) => write_set.clone(),
            TransactionPayload::Program(_) | TransactionPayload::Script(_) | TransactionPayload::Module(_) => unreachable!(
                "write set strategy should only generate write set transactions",
            ),
        };
        let output = test_env.eval_txn(signed_txn)
            .expect("write set transactions should succeed");
        prop_assert_eq!(output.write_set(), &write_set);
    });
}


