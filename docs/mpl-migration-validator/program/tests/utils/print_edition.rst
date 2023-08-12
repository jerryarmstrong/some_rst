program/tests/utils/print_edition.rs
====================================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: rs

    use mpl_token_metadata::{
    id, instruction,
    state::{EDITION, EDITION_MARKER_BIT_SIZE, PREFIX},
};
use solana_program::borsh::try_from_slice_unchecked;
use solana_program_test::{BanksClientError, ProgramTestContext};
use solana_sdk::{
    pubkey::Pubkey, signature::Signer, signer::keypair::Keypair, transaction::Transaction,
};
use spl_associated_token_account::{
    get_associated_token_address, instruction::create_associated_token_account,
};

use crate::*;

#[derive(Debug)]
pub struct TestPrintEdition {
    pub master_mint: Pubkey,
    pub master_metadata: Pubkey,
    pub master_edition: Pubkey,
    pub master_token: Pubkey,
    pub print_mint: Keypair,
    pub print_metadata: Pubkey,
    pub print_edition: Pubkey,
    pub print_token: Keypair,
    pub marker: Pubkey,
    pub edition_number: u64,
}

impl TestPrintEdition {
    pub fn new(nft: &NfTest, edition_number: u64) -> Self {
        let mint = Keypair::new();
        let mint_pubkey = mint.pubkey();
        let metadata_mint_pubkey = nft.mint_pubkey();
        let program_id = id();

        let marker_number = edition_number.checked_div(EDITION_MARKER_BIT_SIZE).unwrap();
        let as_string = marker_number.to_string();
        let (pubkey, _) = Pubkey::find_program_address(
            &[
                PREFIX.as_bytes(),
                program_id.as_ref(),
                metadata_mint_pubkey.as_ref(),
                EDITION.as_bytes(),
                as_string.as_bytes(),
            ],
            &program_id,
        );

        let metadata_seeds = &[PREFIX.as_bytes(), program_id.as_ref(), mint_pubkey.as_ref()];
        let (new_metadata_pubkey, _) = Pubkey::find_program_address(metadata_seeds, &id());

        let master_edition_seeds = &[
            PREFIX.as_bytes(),
            program_id.as_ref(),
            mint_pubkey.as_ref(),
            EDITION.as_bytes(),
        ];
        let (new_edition_pubkey, _) = Pubkey::find_program_address(master_edition_seeds, &id());

        TestPrintEdition {
            master_mint: nft.mint_pubkey(),
            master_metadata: nft.metadata_pubkey(),
            master_edition: nft.edition_pubkey().unwrap(),
            master_token: nft.token_pubkey(),
            print_mint: mint,
            print_metadata: new_metadata_pubkey,
            print_edition: new_edition_pubkey,
            print_token: Keypair::new(),
            marker: pubkey,
            edition_number,
        }
    }

    pub async fn get_data(
        &self,
        context: &mut ProgramTestContext,
    ) -> mpl_token_metadata::state::Metadata {
        let account = get_account(context, &self.marker).await;
        try_from_slice_unchecked(&account.data).unwrap()
    }

    pub async fn create(&self, context: &mut ProgramTestContext) -> Result<(), BanksClientError> {
        create_mint(
            context,
            &self.print_mint,
            &context.payer.pubkey(),
            Some(&context.payer.pubkey()),
            0,
        )
        .await?;
        create_token_account(
            context,
            &self.print_token,
            &self.print_mint.pubkey(),
            &context.payer.pubkey(),
        )
        .await?;
        mint_tokens(
            context,
            &self.print_mint.pubkey(),
            &self.print_token.pubkey(),
            1,
            &context.payer.dirty_clone(),
            None,
        )
        .await?;

        let tx = Transaction::new_signed_with_payer(
            &[instruction::mint_new_edition_from_master_edition_via_token(
                id(),
                self.print_metadata,
                self.print_edition,
                self.master_edition,
                self.print_mint.pubkey(),
                context.payer.pubkey(),
                context.payer.pubkey(),
                context.payer.pubkey(),
                self.master_token,
                context.payer.pubkey(),
                self.master_metadata,
                self.master_mint,
                self.edition_number,
            )],
            Some(&context.payer.pubkey()),
            &[&context.payer, &context.payer],
            context.last_blockhash,
        );

        context
            .banks_client
            .process_transaction_with_commitment(
                tx,
                solana_sdk::commitment_config::CommitmentLevel::Confirmed,
            )
            .await
    }

    pub async fn transfer(
        &mut self,
        context: &mut ProgramTestContext,
        new_owner: &Pubkey,
    ) -> Result<(), BanksClientError> {
        let new_owner_token_account =
            get_associated_token_address(new_owner, &self.print_mint.pubkey());
        let create_token_account_ix = create_associated_token_account(
            &context.payer.pubkey(),
            new_owner,
            &self.print_mint.pubkey(),
            &spl_token::ID,
        );

        let transfer_ix = spl_token::instruction::transfer(
            &spl_token::id(),
            &self.print_token.pubkey(),
            &new_owner_token_account,
            &context.payer.pubkey(),
            &[],
            1,
        )
        .unwrap();

        let transfer_tx = Transaction::new_signed_with_payer(
            &[create_token_account_ix, transfer_ix],
            Some(&context.payer.pubkey()),
            &[&context.payer],
            context.last_blockhash,
        );

        context.banks_client.process_transaction(transfer_tx).await
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
                self.print_metadata,
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

    pub async fn exists_on_chain(&self, context: &mut ProgramTestContext) -> bool {
        // Metadata, Print Edition and token account exist.
        let md_account = context
            .banks_client
            .get_account(self.print_metadata)
            .await
            .unwrap();
        let token_account = context
            .banks_client
            .get_account(self.print_token.pubkey())
            .await
            .unwrap();
        let print_edition_account = context
            .banks_client
            .get_account(self.print_edition)
            .await
            .unwrap();

        md_account.is_some() && token_account.is_some() && print_edition_account.is_some()
    }
}


