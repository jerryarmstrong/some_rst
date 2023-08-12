program/tests/utils/asset.rs
============================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: rs

    use std::collections::HashMap;

use mpl_token_metadata::{
    id,
    instruction::{
        self,
        builders::{CreateBuilder, MintBuilder},
        CreateArgs, InstructionBuilder, MintArgs,
    },
    pda::find_metadata_account,
    state::{AssetData, PrintSupply, TokenStandard},
};
use solana_program_test::{BanksClientError, ProgramTestContext};
use solana_sdk::{
    pubkey::Pubkey, signature::Signer, signer::keypair::Keypair, transaction::Transaction,
};
use spl_associated_token_account::get_associated_token_address;
use spl_token::state::Account as TokenAccount;

pub struct TestAsset {
    pub mint: Keypair,
    pub metadata: Pubkey,
    pub edition: Option<Pubkey>,
    pub token_accounts: HashMap<Pubkey, TokenAccount>,
}

impl Default for TestAsset {
    fn default() -> Self {
        Self::new()
    }
}

impl TestAsset {
    pub fn new() -> Self {
        let mint = Keypair::new();
        let mint_pubkey = mint.pubkey();

        let (metadata, _) = find_metadata_account(&mint_pubkey);

        TestAsset {
            mint,
            metadata,
            edition: None,
            token_accounts: HashMap::new(),
        }
    }

    pub async fn create(
        &self,
        context: &mut ProgramTestContext,
        payer: &Keypair,
        authority: &Keypair,
        token_standard: TokenStandard,
        decimals: u8,
        print_supply: Option<PrintSupply>,
    ) -> Result<(), BanksClientError> {
        let name = "Test Asset".to_string();
        let symbol = "TST".to_string();
        let uri = "https://test.com".to_string();

        let args = CreateArgs::V1 {
            asset_data: AssetData::new(token_standard, name, symbol, uri),
            decimals: Some(decimals),
            print_supply,
        };

        let ix = CreateBuilder::new()
            .mint(self.mint.pubkey())
            .metadata(self.metadata)
            .authority(authority.pubkey())
            .payer(payer.pubkey())
            .update_authority(authority.pubkey())
            .initialize_mint(true)
            .update_authority_as_signer(true)
            .build(args)
            .unwrap()
            .instruction();

        let tx = Transaction::new_signed_with_payer(
            &[ix],
            Some(&payer.pubkey()),
            &[payer, authority, &self.mint],
            context.last_blockhash,
        );

        context.banks_client.process_transaction(tx).await
    }

    pub async fn mint(
        &self,
        context: &mut ProgramTestContext,
        authority: &Keypair,
        owner: Pubkey,
        amount: u64,
    ) -> Result<(), BanksClientError> {
        let args = MintArgs::V1 {
            amount,
            authorization_data: None,
        };

        let token = get_associated_token_address(&owner, &self.mint.pubkey());

        let ix = MintBuilder::new()
            .mint(self.mint.pubkey())
            .metadata(self.metadata)
            .token(token)
            .token_owner(owner)
            .authority(authority.pubkey())
            .payer(authority.pubkey())
            .build(args)
            .unwrap()
            .instruction();

        let tx = Transaction::new_signed_with_payer(
            &[ix],
            Some(&authority.pubkey()),
            &[authority],
            context.last_blockhash,
        );

        context.banks_client.process_transaction(tx).await
    }

    pub async fn mint_default_fungible(
        &self,
        context: &mut ProgramTestContext,
        authority: &Keypair,
    ) -> Result<(), BanksClientError> {
        self.create(
            context,
            authority,
            authority,
            TokenStandard::Fungible,
            0,
            None,
        )
        .await?;
        self.mint(context, authority, authority.pubkey(), 1).await
    }

    pub async fn mint_default_fungible_asset(
        &self,
        context: &mut ProgramTestContext,
        authority: &Keypair,
    ) -> Result<(), BanksClientError> {
        self.create(
            context,
            authority,
            authority,
            TokenStandard::FungibleAsset,
            0,
            None,
        )
        .await?;
        self.mint(context, authority, authority.pubkey(), 1).await
    }

    #[allow(clippy::too_many_arguments)]
    pub async fn set_and_verify_collection(
        &self,
        context: &mut ProgramTestContext,
        collection_metadata: Pubkey,
        collection_authority: &Keypair,
        nft_update_authority: Pubkey,
        collection_mint: Pubkey,
        collection_master_edition_account: Pubkey,
        collection_authority_record: Option<Pubkey>,
    ) -> Result<(), BanksClientError> {
        let tx = Transaction::new_signed_with_payer(
            &[instruction::set_and_verify_collection(
                id(),
                self.metadata,
                collection_authority.pubkey(),
                context.payer.pubkey(),
                nft_update_authority,
                collection_mint,
                collection_metadata,
                collection_master_edition_account,
                collection_authority_record,
            )],
            Some(&context.payer.pubkey()),
            &[&context.payer, collection_authority],
            context.last_blockhash,
        );
        context.banks_client.process_transaction(tx).await
    }
}


