farm-client/src/client/farm_accounts_orca.rs
============================================

Last edited: 2022-12-05 19:44:34

Contents:

.. code-block:: rs

    //! Solana Farm Client Orca Farms accounts builder

use {
    crate::error::FarmClientError,
    solana_farm_sdk::farm::FarmRoute,
    solana_sdk::{
        instruction::AccountMeta, program_error::ProgramError, pubkey::Pubkey, system_program,
    },
    std::vec::Vec,
};

use super::FarmClient;

impl FarmClient {
    /// Returns instruction accounts for initializing a new User in an Orca farm
    pub fn get_user_init_accounts_orca(
        &self,
        wallet_address: &Pubkey,
        farm_name: &str,
    ) -> Result<Vec<AccountMeta>, FarmClientError> {
        // get farm info
        let farm = self.get_farm(farm_name)?;

        let farm_id = match farm.route {
            FarmRoute::Orca { farm_id, .. } => farm_id,
            _ => unreachable!(),
        };

        let farmer = Pubkey::find_program_address(
            &[
                &farm_id.to_bytes(),
                &wallet_address.to_bytes(),
                &spl_token::id().to_bytes(),
            ],
            &farm.farm_program_id,
        )
        .0;

        let accounts = vec![
            AccountMeta::new(*wallet_address, true),
            AccountMeta::new_readonly(*wallet_address, false),
            AccountMeta::new(farmer, false),
            AccountMeta::new_readonly(farm_id, false),
            AccountMeta::new_readonly(farm.farm_program_id, false),
            AccountMeta::new_readonly(system_program::id(), false),
        ];

        Ok(accounts)
    }

    /// Returns instruction accounts for tokens staking in an Orca farm
    pub fn get_stake_accounts_orca(
        &self,
        wallet_address: &Pubkey,
        farm_name: &str,
    ) -> Result<Vec<AccountMeta>, FarmClientError> {
        // get farm info
        let farm = self.get_farm(farm_name)?;

        // get tokens info
        let token_a = self.get_token_by_ref_from_cache(&farm.first_reward_token_ref)?;
        let lp_token = self.get_token_by_ref_from_cache(&farm.lp_token_ref)?;

        // get user accounts info
        let user_reward_token_account = self.get_token_account(wallet_address, &token_a);
        let user_lp_token_account = self.get_token_account(wallet_address, &lp_token);

        // fill in accounts
        let mut accounts = vec![];
        if let FarmRoute::Orca {
            farm_id,
            farm_authority,
            farm_token_ref,
            base_token_vault,
            reward_token_vault,
        } = farm.route
        {
            let user_info_account = self.get_stake_account(wallet_address, farm_name)?;
            let farm_lp_token = self.get_token_by_ref_from_cache(&Some(farm_token_ref))?;
            let user_farm_lp_token_account = self.get_token_account(wallet_address, &farm_lp_token);

            accounts.push(AccountMeta::new_readonly(*wallet_address, true));
            accounts.push(AccountMeta::new(user_info_account, false));
            accounts.push(AccountMeta::new(
                user_lp_token_account.ok_or(ProgramError::UninitializedAccount)?,
                false,
            ));
            accounts.push(AccountMeta::new(
                user_reward_token_account.ok_or(ProgramError::UninitializedAccount)?,
                false,
            ));
            accounts.push(AccountMeta::new(
                user_farm_lp_token_account.ok_or(ProgramError::UninitializedAccount)?,
                false,
            ));
            accounts.push(AccountMeta::new(
                farm_lp_token
                    .ok_or(ProgramError::UninitializedAccount)?
                    .mint,
                false,
            ));
            accounts.push(AccountMeta::new_readonly(farm.farm_program_id, false));
            accounts.push(AccountMeta::new(base_token_vault, false));
            accounts.push(AccountMeta::new(reward_token_vault, false));
            accounts.push(AccountMeta::new_readonly(spl_token::id(), false));
            accounts.push(AccountMeta::new(farm_id, false));
            accounts.push(AccountMeta::new_readonly(farm_authority, false));
        }

        Ok(accounts)
    }

    /// Returns instruction accounts for unstaking tokens from an Orca farm
    pub fn get_unstake_accounts_orca(
        &self,
        wallet_address: &Pubkey,
        farm_name: &str,
    ) -> Result<Vec<AccountMeta>, FarmClientError> {
        // get farm info
        let farm = self.get_farm(farm_name)?;

        // get tokens info
        let token_a = self.get_token_by_ref_from_cache(&farm.first_reward_token_ref)?;
        let lp_token = self.get_token_by_ref_from_cache(&farm.lp_token_ref)?;

        // get user accounts info
        let user_reward_token_account = self.get_token_account(wallet_address, &token_a);
        let user_lp_token_account = self.get_token_account(wallet_address, &lp_token);

        // fill in accounts
        let mut accounts = vec![];
        if let FarmRoute::Orca {
            farm_id,
            farm_authority,
            farm_token_ref,
            base_token_vault,
            reward_token_vault,
        } = farm.route
        {
            let user_info_account = self.get_stake_account(wallet_address, farm_name)?;
            let farm_lp_token = self.get_token_by_ref_from_cache(&Some(farm_token_ref))?;
            let user_farm_lp_token_account = self.get_token_account(wallet_address, &farm_lp_token);

            accounts.push(AccountMeta::new_readonly(*wallet_address, true));
            accounts.push(AccountMeta::new(user_info_account, false));
            accounts.push(AccountMeta::new(
                user_lp_token_account.ok_or(ProgramError::UninitializedAccount)?,
                false,
            ));
            accounts.push(AccountMeta::new(
                user_reward_token_account.ok_or(ProgramError::UninitializedAccount)?,
                false,
            ));
            accounts.push(AccountMeta::new(
                user_farm_lp_token_account.ok_or(ProgramError::UninitializedAccount)?,
                false,
            ));
            accounts.push(AccountMeta::new(
                farm_lp_token
                    .ok_or(ProgramError::UninitializedAccount)?
                    .mint,
                false,
            ));
            accounts.push(AccountMeta::new_readonly(farm.farm_program_id, false));
            accounts.push(AccountMeta::new(base_token_vault, false));
            accounts.push(AccountMeta::new(reward_token_vault, false));
            accounts.push(AccountMeta::new_readonly(spl_token::id(), false));
            accounts.push(AccountMeta::new(farm_id, false));
            accounts.push(AccountMeta::new_readonly(farm_authority, false));
        }

        Ok(accounts)
    }

    /// Returns instruction accounts for rewards harvesting in an Orca farm
    pub fn get_harvest_accounts_orca(
        &self,
        wallet_address: &Pubkey,
        farm_name: &str,
    ) -> Result<Vec<AccountMeta>, FarmClientError> {
        // get farm info
        let farm = self.get_farm(farm_name)?;

        // get tokens info
        let token_a = self.get_token_by_ref_from_cache(&farm.first_reward_token_ref)?;

        // get user accounts info
        let user_reward_token_account = self.get_token_account(wallet_address, &token_a);

        // fill in accounts
        let mut accounts = vec![];
        if let FarmRoute::Orca {
            farm_id,
            farm_authority,
            farm_token_ref: _,
            base_token_vault,
            reward_token_vault,
        } = farm.route
        {
            let user_info_account = self.get_stake_account(wallet_address, farm_name)?;

            accounts.push(AccountMeta::new_readonly(*wallet_address, true));
            accounts.push(AccountMeta::new(user_info_account, false));
            accounts.push(AccountMeta::new(
                user_reward_token_account.ok_or(ProgramError::UninitializedAccount)?,
                false,
            ));
            accounts.push(AccountMeta::new_readonly(farm.farm_program_id, false));
            accounts.push(AccountMeta::new(base_token_vault, false));
            accounts.push(AccountMeta::new(reward_token_vault, false));
            accounts.push(AccountMeta::new_readonly(spl_token::id(), false));
            accounts.push(AccountMeta::new(farm_id, false));
            accounts.push(AccountMeta::new_readonly(farm_authority, false));
        }

        Ok(accounts)
    }
}


