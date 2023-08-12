program/src/instruction.rs
==========================

Last edited: 2023-08-01 14:25:31

Contents:

.. code-block:: rs

    use borsh::{BorshDeserialize, BorshSerialize};
use mpl_token_metadata::{
    pda::{find_master_edition_account, find_metadata_account, find_token_record_account},
    processor::AuthorizationData,
};
use shank::ShankInstruction;

use super::*;

#[repr(C)]
#[derive(BorshSerialize, BorshDeserialize, PartialEq, Eq, Debug, Clone)]
pub struct WithdrawArgs {
    pub auth_data: AuthorizationData,
}

#[repr(C)]
#[derive(BorshSerialize, BorshDeserialize, PartialEq, Eq, Debug, Clone)]
pub struct DelegateArgs {
    pub amount: u64,
    pub authority: Pubkey,
    pub bump: u8,
}

#[repr(C)]
#[derive(BorshSerialize, BorshDeserialize, PartialEq, Eq, Debug, Clone)]
pub struct LockArgs {
    pub amount: u64,
    pub bump: u8,
}

#[repr(C)]
#[derive(BorshSerialize, BorshDeserialize, PartialEq, Eq, Debug, Clone)]
pub struct UnlockArgs {
    pub bump: u8,
}

#[derive(BorshSerialize, BorshDeserialize, PartialEq, Eq, Debug, Clone)]
pub struct DelegateTransferArgs {
    pub amount: u64,
    pub auth_data: AuthorizationData,
}

#[derive(Debug, Clone, ShankInstruction, BorshSerialize, BorshDeserialize)]
#[rustfmt::skip]
pub enum RoosterCommand {
    /// Initialize a new rooster
    #[account(0, writable, signer, name="authority", desc="Account owner")]
    #[account(1, writable, name="rooster_pda", desc = "Rooster PDA account")]
    #[account(2, name="system_program", desc = "The system program")]
    Init,

    /// Withdraw the token from the rooster by CPIing into Token Metadata 'Transfer'
    #[account(0, writable, signer, name="authority", desc="Account owner")]
    #[account(1, writable, name="rooster_pda", desc = "Rooster PDA account")]
    #[account(2, writable, name="token", desc = "Token account for rooster PDA")]
    #[account(3, name="destination_owner", desc = "Owner of the destination token account")]
    #[account(4, writable, name="destination", desc = "Destination token account")]
    #[account(5, name="mint", desc = "Token mint")]
    #[account(6, writable, name="metadata", desc = "Token metadata account")]
    #[account(7, name="edition", desc = "Token edition account")]
    #[account(8, name="token_record", desc = "Token record account")]
    #[account(9, name="token_metadata_program", desc = "The token metadata program")]
    #[account(10, name="system_program", desc = "The system program")]
    #[account(11, name="sysvar_instructions", desc = "The sysvar instructions")]
    #[account(12, name="spl_token_program", desc = "The token program")]
    #[account(13, name="spl_ata_program", desc = "The spl ata program")]
    #[account(14, name="authorization_rules_program", desc = "The authorization rules program")]
    #[account(15, name="authorization_rules", desc = "The authorization rules PDA account")]
    Withdraw(WithdrawArgs),

    /// Create delegate via Token Metadata CPI
    #[account(0, writable, signer, name="delegate", desc="Delegate account")]
    #[account(1, writable, name="rooster_pda", desc = "Rooster PDA account")]
    #[account(2, writable, name="token", desc = "Token account for rooster PDA")]
    #[account(3, name="mint", desc = "Token mint")]
    #[account(4, writable, name="metadata", desc = "Token metadata account")]
    #[account(5, name="edition", desc = "Token edition account")]
    #[account(6, name="delegate_record", desc = "Collection delegate record account")]
    #[account(7, name="token_metadata_program", desc = "The token metadata program")]
    #[account(8, name="system_program", desc = "The system program")]
    #[account(9, name="sysvar_instructions", desc = "The sysvar instructions")]
    #[account(10, name="spl_token_program", desc = "The token program")]
    #[account(11, name="authorization_rules_program", desc="Token Authorization Rules Program")]
    #[account(12, name="authorization_rules", desc="Token Authorization Rules account")]
    Delegate(DelegateArgs),
    
    /// Locks a (non-programmable) token inplace via Token Metadata CPI
    #[account(0, name="delegate", desc="Delegate PDA")]
    #[account(1, signer, name="token_owner", desc="Token owner")]
    #[account(2, writable, name="token", desc="Token account")]
    #[account(3, name="mint", desc="Mint account")]
    #[account(4, writable, name="metadata", desc="Metadata account")]
    #[account(5, name="edition", desc="Edition account")]
    #[account(6, name="token_metadata_program", desc = "The token metadata program")]
    #[account(7, name="system_program", desc="System program")]
    #[account(8, name="sysvar_instructions", desc="System program")]
    #[account(9, name="spl_token_program", desc="SPL Token Program")]
    Lock(LockArgs),

    /// Unlocks a (non-programmable) token inplace via Token Metadata CPI
    #[account(0, name="delegate", desc="Delegate PDA")]
    #[account(1, signer, name="token_owner", desc="Token owner")]
    #[account(2, writable, name="token", desc="Token account")]
    #[account(3, name="mint", desc="Mint account")]
    #[account(4, writable, name="metadata", desc="Metadata account")]
    #[account(5, name="edition", desc="Edition account")]
    #[account(6, name="token_metadata_program", desc = "The token metadata program")]
    #[account(7, name="system_program", desc="System program")]
    #[account(8, name="sysvar_instructions", desc="System program")]
    #[account(9, name="spl_token_program", desc="SPL Token Program")]
    Unlock(UnlockArgs),

    /// Locks a (non-programmable) token inplace via Token Metadata CPI
    #[account(0, name="delegate", desc="Delegate PDA")]
    #[account(1, signer, name="token_owner", desc="Token owner")]
    #[account(2, writable, name="token", desc="Token account")]
    #[account(3, name="mint", desc="Mint account")]
    #[account(4, writable, name="metadata", desc="Metadata account")]
    #[account(5, name="edition", desc="Edition account")]
    #[account(6, writable, name="token_record", desc="Token record account")]
    #[account(7, name="token_metadata_program", desc = "The token metadata program")]
    #[account(8, name="system_program", desc="System program")]
    #[account(9, name="sysvar_instructions", desc="System program")]
    #[account(10, name="spl_token_program", desc="SPL Token Program")]
    #[account(11, name="authorization_rules_program", desc="Token Authorization Rules Program")]
    #[account(12, name="authorization_rules", desc="Token Authorization Rules account")]
    ProgrammableLock(LockArgs),

    /// Unlocks a (non-programmable) token inplace via Token Metadata CPI
    #[account(0, name="delegate", desc="Delegate PDA")]
    #[account(1, signer, name="token_owner", desc="Token owner")]
    #[account(2, writable, name="token", desc="Token account")]
    #[account(3, name="mint", desc="Mint account")]
    #[account(4, writable, name="metadata", desc="Metadata account")]
    #[account(5, name="edition", desc="Edition account")]
    #[account(6, writable, name="token_record", desc="Token record account")]
    #[account(7, name="token_metadata_program", desc = "The token metadata program")]
    #[account(8, name="system_program", desc="System program")]
    #[account(9, name="sysvar_instructions", desc="System program")]
    #[account(10, name="spl_token_program", desc="SPL Token Program")]
    #[account(11, name="authorization_rules_program", desc="Token Authorization Rules Program")]
    #[account(12, name="authorization_rules", desc="Token Authorization Rules account")]
    ProgrammableUnlock(UnlockArgs),

    /// Delegate transfer
    #[account(0, writable, signer, name="authority", desc="Account owner")]
    #[account(1, writable, name="rooster_pda", desc = "Rooster PDA account as a delegate")]
    #[account(2, writable, name="source_owner", desc = "Owner of the source token account")]
    #[account(3, writable, name="source_token", desc = "Source token account")]
    #[account(4, name="destination_owner", desc = "Owner of the destination token account")]
    #[account(5, writable, name="destination_token", desc = "Destination token account")]
    #[account(6, name="mint", desc = "Token mint")]
    #[account(7, writable, name="metadata", desc = "Token metadata account")]
    #[account(8, name="edition", desc = "Token edition account")]
    #[account(9, name="source_token_record", desc = "Source Token record account")]
    #[account(10, name="dest_token_record", desc = "Destination Token record account")]
    #[account(11, name="token_metadata_program", desc = "The token metadata program")]
    #[account(12, name="system_program", desc = "The system program")]
    #[account(13, name="sysvar_instructions", desc = "The sysvar instructions")]
    #[account(14, name="spl_token_program", desc = "The token program")]
    #[account(15, name="spl_ata_program", desc = "The spl ata program")]
    #[account(16, name="authorization_rules_program", desc = "The authorization rules program")]
    #[account(17, name="authorization_rules", desc = "The authorization rules PDA account")]
    DelegateTransfer(DelegateTransferArgs),
}

pub fn init(authority: Pubkey, rooster_pda: Pubkey) -> Instruction {
    Instruction {
        program_id: crate::ID,
        accounts: vec![
            AccountMeta::new(authority, true),
            AccountMeta::new(rooster_pda, false),
            AccountMeta::new_readonly(solana_program::system_program::id(), false),
        ],
        data: RoosterCommand::Init.try_to_vec().unwrap(),
    }
}

#[allow(clippy::too_many_arguments)]
pub fn withdraw(
    authority: Pubkey,
    rooster_pda: Pubkey,
    token: Pubkey,
    destination_owner: Pubkey,
    destination: Pubkey,
    mint: Pubkey,
    metadata: Pubkey,
    edition: Pubkey,
    rule_set: Pubkey,
    spl_token_program: Pubkey,
    args: WithdrawArgs,
) -> Instruction {
    let (owner_token_record, _) = find_token_record_account(&mint, &token);
    let (destination_token_record, _) = find_token_record_account(&mint, &destination);

    Instruction {
        program_id: crate::ID,
        accounts: vec![
            AccountMeta::new(authority, true),
            AccountMeta::new(rooster_pda, false),
            AccountMeta::new(token, false),
            AccountMeta::new_readonly(destination_owner, false),
            AccountMeta::new(destination, false),
            AccountMeta::new(mint, false),
            AccountMeta::new(metadata, false),
            AccountMeta::new(edition, false),
            AccountMeta::new(owner_token_record, false),
            AccountMeta::new(destination_token_record, false),
            AccountMeta::new_readonly(mpl_token_metadata::ID, false),
            AccountMeta::new_readonly(solana_program::system_program::id(), false),
            AccountMeta::new_readonly(solana_program::sysvar::instructions::id(), false),
            AccountMeta::new_readonly(spl_token_program, false),
            AccountMeta::new_readonly(SPL_ATA_TOKEN_PROGRAM_ID, false),
            AccountMeta::new_readonly(MPL_TOKEN_AUTH_RULES_PROGRAM_ID, false),
            AccountMeta::new_readonly(rule_set, false),
        ],
        data: RoosterCommand::Withdraw(args).try_to_vec().unwrap(),
    }
}

#[allow(clippy::too_many_arguments)]
pub fn delegate(
    delegate: Pubkey,
    rooster_pda: Pubkey,
    token: Pubkey,
    mint: Pubkey,
    metadata: Pubkey,
    edition: Pubkey,
    authorization_rules: Option<Pubkey>,
    spl_token_program: Pubkey,
    args: DelegateArgs,
) -> Instruction {
    let (token_record, _bump) = find_token_record_account(&mint, &token);

    Instruction {
        program_id: crate::ID,
        accounts: vec![
            AccountMeta::new(delegate, true),
            AccountMeta::new(rooster_pda, false),
            AccountMeta::new(token, false),
            AccountMeta::new_readonly(mint, false),
            AccountMeta::new(metadata, false),
            AccountMeta::new_readonly(edition, false),
            AccountMeta::new(token_record, false),
            AccountMeta::new_readonly(mpl_token_metadata::ID, false),
            AccountMeta::new_readonly(solana_program::system_program::id(), false),
            AccountMeta::new_readonly(solana_program::sysvar::instructions::id(), false),
            AccountMeta::new_readonly(spl_token_program, false),
            AccountMeta::new_readonly(MPL_TOKEN_AUTH_RULES_PROGRAM_ID, false),
            AccountMeta::new_readonly(
                authorization_rules.ok_or(mpl_token_metadata::ID).unwrap(),
                false,
            ),
        ],
        data: RoosterCommand::Delegate(args).try_to_vec().unwrap(),
    }
}

#[allow(clippy::too_many_arguments)]
pub fn lock(
    authority: Pubkey,
    token_owner: Pubkey,
    token: Pubkey,
    mint: Pubkey,
    metadata: Pubkey,
    edition: Pubkey,
    spl_token_program: Pubkey,
    args: LockArgs,
) -> Instruction {
    Instruction {
        program_id: crate::ID,
        accounts: vec![
            AccountMeta::new(authority, false),
            AccountMeta::new(token_owner, true),
            AccountMeta::new(token, false),
            AccountMeta::new_readonly(mint, false),
            AccountMeta::new(metadata, false),
            AccountMeta::new_readonly(edition, false),
            AccountMeta::new_readonly(mpl_token_metadata::ID, false),
            AccountMeta::new_readonly(solana_program::system_program::id(), false),
            AccountMeta::new_readonly(solana_program::sysvar::instructions::id(), false),
            AccountMeta::new_readonly(spl_token_program, false),
            AccountMeta::new_readonly(MPL_TOKEN_AUTH_RULES_PROGRAM_ID, false),
            AccountMeta::new_readonly(mpl_token_metadata::ID, false),
        ],
        data: RoosterCommand::Lock(args).try_to_vec().unwrap(),
    }
}

#[allow(clippy::too_many_arguments)]
pub fn unlock(
    authority: Pubkey,
    token_owner: Pubkey,
    token: Pubkey,
    mint: Pubkey,
    metadata: Pubkey,
    edition: Pubkey,
    spl_token_program: Pubkey,
    args: UnlockArgs,
) -> Instruction {
    Instruction {
        program_id: crate::ID,
        accounts: vec![
            AccountMeta::new(authority, false),
            AccountMeta::new(token_owner, true),
            AccountMeta::new(token, false),
            AccountMeta::new_readonly(mint, false),
            AccountMeta::new(metadata, false),
            AccountMeta::new_readonly(edition, false),
            AccountMeta::new_readonly(mpl_token_metadata::ID, false),
            AccountMeta::new_readonly(solana_program::system_program::id(), false),
            AccountMeta::new_readonly(solana_program::sysvar::instructions::id(), false),
            AccountMeta::new_readonly(spl_token_program, false),
            AccountMeta::new_readonly(MPL_TOKEN_AUTH_RULES_PROGRAM_ID, false),
            AccountMeta::new_readonly(mpl_token_metadata::ID, false),
        ],
        data: RoosterCommand::Unlock(args).try_to_vec().unwrap(),
    }
}

#[allow(clippy::too_many_arguments)]
pub fn programmable_lock(
    authority: Pubkey,
    token_owner: Pubkey,
    token: Pubkey,
    mint: Pubkey,
    metadata: Pubkey,
    edition: Pubkey,
    authorization_rules: Option<Pubkey>,
    spl_token_program: Pubkey,
    args: LockArgs,
) -> Instruction {
    let (token_record, _) = find_token_record_account(&mint, &token);

    Instruction {
        program_id: crate::ID,
        accounts: vec![
            AccountMeta::new(authority, false),
            AccountMeta::new(token_owner, true),
            AccountMeta::new(token, false),
            AccountMeta::new_readonly(mint, false),
            AccountMeta::new(metadata, false),
            AccountMeta::new_readonly(edition, false),
            AccountMeta::new(token_record, false),
            AccountMeta::new_readonly(mpl_token_metadata::ID, false),
            AccountMeta::new_readonly(solana_program::system_program::id(), false),
            AccountMeta::new_readonly(solana_program::sysvar::instructions::id(), false),
            AccountMeta::new_readonly(spl_token_program, false),
            AccountMeta::new_readonly(MPL_TOKEN_AUTH_RULES_PROGRAM_ID, false),
            AccountMeta::new_readonly(
                authorization_rules.ok_or(mpl_token_metadata::ID).unwrap(),
                false,
            ),
        ],
        data: RoosterCommand::ProgrammableLock(args).try_to_vec().unwrap(),
    }
}

#[allow(clippy::too_many_arguments)]
pub fn programmable_unlock(
    authority: Pubkey,
    token_owner: Pubkey,
    token: Pubkey,
    mint: Pubkey,
    metadata: Pubkey,
    edition: Pubkey,
    authorization_rules: Option<Pubkey>,
    spl_token_program: Pubkey,
    args: UnlockArgs,
) -> Instruction {
    let (token_record, _) = find_token_record_account(&mint, &token);

    Instruction {
        program_id: crate::ID,
        accounts: vec![
            AccountMeta::new(authority, false),
            AccountMeta::new(token_owner, true),
            AccountMeta::new(token, false),
            AccountMeta::new_readonly(mint, false),
            AccountMeta::new(metadata, false),
            AccountMeta::new_readonly(edition, false),
            AccountMeta::new(token_record, false),
            AccountMeta::new_readonly(mpl_token_metadata::ID, false),
            AccountMeta::new_readonly(solana_program::system_program::id(), false),
            AccountMeta::new_readonly(solana_program::sysvar::instructions::id(), false),
            AccountMeta::new_readonly(spl_token_program, false),
            AccountMeta::new_readonly(MPL_TOKEN_AUTH_RULES_PROGRAM_ID, false),
            AccountMeta::new_readonly(
                authorization_rules.ok_or(mpl_token_metadata::ID).unwrap(),
                false,
            ),
        ],
        data: RoosterCommand::ProgrammableUnlock(args)
            .try_to_vec()
            .unwrap(),
    }
}

#[allow(clippy::too_many_arguments)]
pub fn delegate_transfer(
    authority: Pubkey,
    rooster_pda: Pubkey,
    source_owner: Pubkey,
    source_token: Pubkey,
    destination_owner: Pubkey,
    destination_token: Pubkey,
    mint: Pubkey,
    rule_set: Pubkey,
    spl_token_program: Pubkey,
    args: DelegateTransferArgs,
) -> Instruction {
    let (metadata, _) = find_metadata_account(&mint);
    let (edition, _) = find_master_edition_account(&mint);
    let (source_token_record, _) = find_token_record_account(&mint, &source_token);
    let (destination_token_record, _) = find_token_record_account(&mint, &destination_token);

    Instruction {
        program_id: crate::ID,
        accounts: vec![
            AccountMeta::new(authority, true),
            AccountMeta::new(rooster_pda, false),
            AccountMeta::new(source_owner, false),
            AccountMeta::new(source_token, false),
            AccountMeta::new_readonly(destination_owner, false),
            AccountMeta::new(destination_token, false),
            AccountMeta::new(mint, false),
            AccountMeta::new(metadata, false),
            AccountMeta::new(edition, false),
            AccountMeta::new(source_token_record, false),
            AccountMeta::new(destination_token_record, false),
            AccountMeta::new_readonly(mpl_token_metadata::ID, false),
            AccountMeta::new_readonly(solana_program::system_program::id(), false),
            AccountMeta::new_readonly(solana_program::sysvar::instructions::id(), false),
            AccountMeta::new_readonly(spl_token_program, false),
            AccountMeta::new_readonly(SPL_ATA_TOKEN_PROGRAM_ID, false),
            AccountMeta::new_readonly(MPL_TOKEN_AUTH_RULES_PROGRAM_ID, false),
            AccountMeta::new_readonly(rule_set, false),
        ],
        data: RoosterCommand::DelegateTransfer(args).try_to_vec().unwrap(),
    }
}


