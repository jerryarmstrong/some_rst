governance/chat/program/tests/program_test/cookies.rs
=====================================================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: rs

    use solana_program::pubkey::Pubkey;
use solana_sdk::signature::Keypair;
use spl_governance_chat::state::ChatMessage;

#[derive(Debug)]
pub struct ChatMessageCookie {
    pub address: Pubkey,
    pub account: ChatMessage,
}

#[derive(Debug)]
pub struct ProposalCookie {
    pub address: Pubkey,
    pub realm_address: Pubkey,
    pub governance_address: Pubkey,
    pub token_owner_record_address: Pubkey,
    pub token_owner: Keypair,

    pub governing_token_mint: Pubkey,
    pub governing_token_mint_authority: Keypair,

    pub voter_weight_record: Option<Pubkey>,
}

#[derive(Debug)]
pub struct TokenOwnerRecordCookie {
    pub address: Pubkey,
    pub token_owner: Keypair,
}


