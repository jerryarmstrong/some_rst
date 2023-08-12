program/tests/utils/mod.rs
==========================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: rs

    use async_trait::async_trait;
use solana_program::{program_pack::Pack, pubkey::Pubkey, system_instruction};
use solana_program_test::{BanksClientError, ProgramTest, ProgramTestContext};
use solana_sdk::{account::Account, signature::Keypair, signer::Signer, transaction::Transaction};

mod assert;
mod asset;
mod migratorr;
mod nft;
mod print_edition;
mod programmable;

pub use assert::*;
pub use asset::*;
pub use migratorr::*;
pub use nft::*;
pub use print_edition::*;
pub use programmable::*;

pub trait DirtyClone {
    fn dirty_clone(&self) -> Self;
}

impl DirtyClone for Keypair {
    fn dirty_clone(&self) -> Self {
        Keypair::from_bytes(&self.to_bytes()).unwrap()
    }
}

#[async_trait]
pub trait Airdrop {
    async fn airdrop(
        &self,
        context: &mut ProgramTestContext,
        lamports: u64,
    ) -> Result<(), BanksClientError>;
}

#[async_trait]
impl Airdrop for Keypair {
    async fn airdrop(
        &self,
        context: &mut ProgramTestContext,
        lamports: u64,
    ) -> Result<(), BanksClientError> {
        let tx = Transaction::new_signed_with_payer(
            &[system_instruction::transfer(
                &context.payer.pubkey(),
                &self.pubkey(),
                lamports,
            )],
            Some(&context.payer.pubkey()),
            &[&context.payer],
            context.last_blockhash,
        );

        context.banks_client.process_transaction(tx).await
    }
}

pub async fn warp100(context: &mut ProgramTestContext) {
    let current_slot = context.banks_client.get_root_slot().await.unwrap();
    println!("Warping to slot: {}", current_slot + 100);
    context.warp_to_slot(current_slot + 100).unwrap();
}

pub async fn setup_context() -> ProgramTestContext {
    let mut test = ProgramTest::new("mpl_migration_validator", mpl_migration_validator::ID, None);
    test.add_program("mpl_token_metadata", mpl_token_metadata::ID, None);
    test.start_with_context().await
}

pub async fn setup_pnft_context() -> ProgramTestContext {
    let mut test = ProgramTest::new("mpl_migration_validator", mpl_migration_validator::ID, None);
    test.add_program("mpl_token_metadata", mpl_token_metadata::ID, None);
    test.add_program("mpl_token_auth_rules", mpl_token_auth_rules::ID, None);
    test.start_with_context().await
}

pub async fn get_account(context: &mut ProgramTestContext, pubkey: &Pubkey) -> Account {
    context
        .banks_client
        .get_account(*pubkey)
        .await
        .expect("account not found")
        .expect("account empty")
}

pub async fn mint_tokens(
    context: &mut ProgramTestContext,
    mint: &Pubkey,
    account: &Pubkey,
    amount: u64,
    owner: &Keypair,
    additional_signer: Option<&Keypair>,
) -> Result<(), BanksClientError> {
    let mut signing_keypairs = vec![&context.payer, owner];
    if let Some(signer) = additional_signer {
        signing_keypairs.push(signer);
    }

    let tx = Transaction::new_signed_with_payer(
        &[spl_token::instruction::mint_to(
            &spl_token::id(),
            mint,
            account,
            &owner.pubkey(),
            &[],
            amount,
        )
        .unwrap()],
        Some(&context.payer.pubkey()),
        &signing_keypairs,
        context.last_blockhash,
    );

    context.banks_client.process_transaction(tx).await
}

pub async fn create_token_account(
    context: &mut ProgramTestContext,
    account: &Keypair,
    mint: &Pubkey,
    manager: &Pubkey,
) -> Result<(), BanksClientError> {
    let rent = context.banks_client.get_rent().await.unwrap();

    let tx = Transaction::new_signed_with_payer(
        &[
            system_instruction::create_account(
                &context.payer.pubkey(),
                &account.pubkey(),
                rent.minimum_balance(spl_token::state::Account::LEN),
                spl_token::state::Account::LEN as u64,
                &spl_token::id(),
            ),
            spl_token::instruction::initialize_account(
                &spl_token::id(),
                &account.pubkey(),
                mint,
                manager,
            )
            .unwrap(),
        ],
        Some(&context.payer.pubkey()),
        &[&context.payer, account],
        context.last_blockhash,
    );

    context.banks_client.process_transaction(tx).await
}

pub async fn create_mint(
    context: &mut ProgramTestContext,
    mint: &Keypair,
    manager: &Pubkey,
    freeze_authority: Option<&Pubkey>,
    decimals: u8,
) -> Result<(), BanksClientError> {
    let rent = context.banks_client.get_rent().await.unwrap();

    let tx = Transaction::new_signed_with_payer(
        &[
            system_instruction::create_account(
                &context.payer.pubkey(),
                &mint.pubkey(),
                rent.minimum_balance(spl_token::state::Mint::LEN),
                spl_token::state::Mint::LEN as u64,
                &spl_token::id(),
            ),
            spl_token::instruction::initialize_mint(
                &spl_token::id(),
                &mint.pubkey(),
                manager,
                freeze_authority,
                decimals,
            )
            .unwrap(),
        ],
        Some(&context.payer.pubkey()),
        &[&context.payer, mint],
        context.last_blockhash,
    );

    context.banks_client.process_transaction(tx).await
}

pub fn find_migrate_state_pda(mint: &Pubkey) -> (Pubkey, u8) {
    let seeds = &[b"migration", mint.as_ref()];
    Pubkey::find_program_address(seeds, &mpl_migration_validator::ID)
}

pub fn find_program_signer_pda() -> (Pubkey, u8) {
    Pubkey::find_program_address(&[b"signer"], &mpl_migration_validator::ID)
}


