language/e2e_tests/src/tests/account_universe/rotate_key.rs
===========================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use crate::{
    account_universe::{
        default_num_accounts, default_num_transactions, AccountUniverseGen, RotateKeyGen,
    },
    gas_costs,
    tests::account_universe::{run_and_assert_gas_cost_stability, run_and_assert_universe},
};
use proptest::{collection::vec, prelude::*};

proptest! {
    // These tests are pretty slow but quite comprehensive, so run a smaller number of them.
    #![proptest_config(ProptestConfig::with_cases(32))]

    #[test]
    fn rotate_key_gas_cost_stability(
        universe in AccountUniverseGen::success_strategy(1),
        key_rotations in vec(any::<RotateKeyGen>(), 0..default_num_transactions()),
    ) {
        run_and_assert_gas_cost_stability(universe, key_rotations, *gas_costs::ROTATE_KEY)?;
    }

    #[test]
    fn rotate_key_high_balance(
        universe in AccountUniverseGen::strategy(
            1..default_num_accounts(),
            1_000_000u64..10_000_000,
        ),
        key_rotations in vec(any::<RotateKeyGen>(), 0..default_num_transactions()),
    ) {
        run_and_assert_universe(universe, key_rotations)?;
    }

    #[test]
    fn rotate_key_low_balance(
        universe in AccountUniverseGen::strategy(1..default_num_accounts(), 0u64..100_000),
        key_rotations in vec(any::<RotateKeyGen>(), 0..default_num_transactions()),
    ) {
        run_and_assert_universe(universe, key_rotations)?;
    }
}


