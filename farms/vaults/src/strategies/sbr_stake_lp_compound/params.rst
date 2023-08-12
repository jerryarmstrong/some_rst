farms/vaults/src/strategies/sbr_stake_lp_compound/params.rs
===========================================================

Last edited: 2022-07-07 18:10:20

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


