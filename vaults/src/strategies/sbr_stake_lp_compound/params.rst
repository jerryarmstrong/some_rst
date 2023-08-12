vaults/src/strategies/sbr_stake_lp_compound/params.rs
=====================================================

Last edited: 2022-12-05 19:44:34

Contents:

.. code-block:: rs

    //! Vault related parameters and accounts

use crate::{traits::VaultParams, vault_info::VaultInfo};

impl VaultParams for VaultInfo<'_, '_> {
    fn default_min_crank_interval() -> u64 {
        60
    }

    fn default_fee() -> f64 {
        0.003
    }

    fn default_external_fee() -> f64 {
        0.0025
    }
}


