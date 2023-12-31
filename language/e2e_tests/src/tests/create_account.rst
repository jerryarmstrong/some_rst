language/e2e_tests/src/tests/create_account.rs
==============================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use crate::{
    account::{Account, AccountData},
    common_transactions::create_account_txn,
    executor::test_all_genesis,
};
use solana_libra_types::{
    transaction::{SignedTransaction, TransactionStatus},
    vm_error::{StatusCode, VMStatus},
};

#[test]
fn create_account() {
    // create a FakeExecutor with a genesis from file
    test_all_genesis(|mut executor| {
        // create and publish a sender with 1_000_000 coins
        let sender = AccountData::new(1_000_000, 10);
        executor.add_account_data(&sender);
        let new_account = Account::new();
        let initial_amount = 1_000;
        let txn = create_account_txn(sender.account(), &new_account, 10, initial_amount);

        // execute transaction
        let txns: Vec<SignedTransaction> = vec![txn];
        let output = executor.execute_block(txns);
        let txn_output = output.get(0).expect("must have a transaction output");
        assert_eq!(
            output[0].status(),
            &TransactionStatus::Keep(VMStatus::new(StatusCode::EXECUTED))
        );
        println!("write set {:?}", txn_output.write_set());
        executor.apply_write_set(txn_output.write_set());

        // check that numbers in stored DB are correct
        let gas = txn_output.gas_used();
        let sender_balance = 1_000_000 - initial_amount - gas;
        let updated_sender = executor
            .read_account_resource(sender.account())
            .expect("sender must exist");
        let updated_receiver = executor
            .read_account_resource(&new_account)
            .expect("receiver must exist");
        assert_eq!(initial_amount, updated_receiver.balance(),);
        assert_eq!(sender_balance, updated_sender.balance(),);
        assert_eq!(11, updated_sender.sequence_number());
    });
}

#[test]
fn create_account_zero_balance() {
    // create a FakeExecutor with a genesis from file
    test_all_genesis(|mut executor| {
        // create and publish a sender with 1_000_000 coins
        let sender = AccountData::new(1_000_000, 10);
        executor.add_account_data(&sender);
        let new_account = Account::new();

        // define the arguments to the create account transaction
        let initial_amount = 0;
        let txn = create_account_txn(sender.account(), &new_account, 10, initial_amount);

        // execute transaction
        let txns: Vec<SignedTransaction> = vec![txn];
        let output = executor.execute_block(txns);
        let txn_output = output.get(0).expect("must have a transaction output");
        assert_eq!(
            output[0].status(),
            &TransactionStatus::Keep(VMStatus::new(StatusCode::EXECUTED))
        );
        println!("write set {:?}", txn_output.write_set());
        executor.apply_write_set(txn_output.write_set());

        // check that numbers in stored DB are correct
        let gas = txn_output.gas_used();
        let sender_balance = 1_000_000 - initial_amount - gas;
        let updated_sender = executor
            .read_account_resource(sender.account())
            .expect("sender must exist");
        let updated_receiver = executor
            .read_account_resource(&new_account)
            .expect("receiver must exist");
        assert_eq!(initial_amount, updated_receiver.balance());
        assert_eq!(sender_balance, updated_sender.balance());
        assert_eq!(11, updated_sender.sequence_number());
    });
}


