program/tests/utils/nft.rs
==========================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: rs

    use mpl_token_metadata::{
    id,
    instruction::{self, builders::UpdateBuilder, InstructionBuilder, UpdateArgs},
    pda::find_token_record_account,
    state::{
        Collection, CollectionDetails, Creator, ProgrammableConfig, TokenDelegateRole,
        TokenMetadataAccount, TokenRecord, TokenStandard, TokenState, Uses, EDITION, PREFIX,
    },
};
use solana_program::{borsh::try_from_slice_unchecked, program_pack::Pack};
use solana_program_test::{BanksClientError, ProgramTestContext};
use solana_sdk::{
    pubkey::Pubkey, signature::Signer, signer::keypair::Keypair, transaction::Transaction,
};
use spl_token::state::Account as TokenAccount;

use super::*;

// This test struct is defined by the mint account.
// Edition and Metadata are derived from the mint and the mint should
// never change for this object.
// Token accounts and token record values can be updated and can be refreshed
// by calling nft.refresh_accounts()
#[derive(Debug)]
pub struct NfTest {
    mint: Keypair,
    metadata: Pubkey,
    edition: Option<Pubkey>,
    token: Keypair,
    token_account: Option<TokenAccount>,
    token_record: Option<TokenRecord>,
}

pub struct MintArgs {
    authority: Keypair,
    name: String,
    symbol: String,
    uri: String,
    creators: Option<Vec<Creator>>,
    seller_fee_basis_points: u16,
    is_mutable: bool,
    collection: Option<Collection>,
    uses: Option<Uses>,
    collection_details: Option<CollectionDetails>,
}

impl MintArgs {
    pub fn new() -> Self {
        MintArgs {
            authority: Keypair::new(),
            name: "name".to_string(),
            symbol: "symbol".to_string(),
            uri: "uri".to_string(),
            creators: None,
            seller_fee_basis_points: 0,
            is_mutable: true,
            collection: None,
            uses: None,
            collection_details: None,
        }
    }
}

impl Default for MintArgs {
    fn default() -> Self {
        MintArgs::new()
    }
}

pub struct SetAndVerifyCollectionArgs {
    pub collection_metadata: Pubkey,
    pub collection_authority: Keypair,
    pub nft_update_authority: Pubkey,
    pub collection_mint: Pubkey,
    pub collection_master_edition_account: Pubkey,
    pub collection_authority_record: Option<Pubkey>,
}

pub struct SetNewUpdateAuthorityArgs {
    pub update_authority: Keypair,
    pub new_update_authority: Pubkey,
}

impl NfTest {
    pub fn new() -> Self {
        let mint = Keypair::new();
        let mint_pubkey = mint.pubkey();
        let program_id = id();

        let metadata_seeds = &[PREFIX.as_bytes(), program_id.as_ref(), mint_pubkey.as_ref()];
        let (metadata, _) = Pubkey::find_program_address(metadata_seeds, &id());

        NfTest {
            mint,
            metadata,
            edition: None,
            token: Keypair::new(),
            token_account: None,
            token_record: None,
        }
    }

    pub fn mint_pubkey(&self) -> Pubkey {
        self.mint.pubkey()
    }

    pub fn mint_keypair(&self) -> &Keypair {
        &self.mint
    }

    pub fn metadata_pubkey(&self) -> Pubkey {
        self.metadata
    }

    pub fn edition_pubkey(&self) -> Option<Pubkey> {
        self.edition
    }

    pub fn token_pubkey(&self) -> Pubkey {
        self.token.pubkey()
    }

    pub fn token_keypair(&self) -> &Keypair {
        &self.token
    }

    pub fn set_mint(&mut self, mint: Keypair) {
        self.mint = mint;
    }

    pub fn set_metadata(&mut self, metadata: Pubkey) {
        self.metadata = metadata;
    }

    pub async fn get_data(
        &self,
        context: &mut ProgramTestContext,
    ) -> mpl_token_metadata::state::Metadata {
        let account = get_account(context, &self.metadata).await;
        mpl_token_metadata::state::Metadata::safe_deserialize(&account.data).unwrap()
    }

    pub async fn mint(
        &self,
        context: &mut ProgramTestContext,
        args: MintArgs,
    ) -> Result<(), BanksClientError> {
        create_mint(
            context,
            &self.mint,
            &args.authority.pubkey(),
            Some(&args.authority.pubkey()),
            0,
        )
        .await?;
        create_token_account(
            context,
            &self.token,
            &self.mint.pubkey(),
            &args.authority.pubkey(),
        )
        .await?;
        mint_tokens(
            context,
            &self.mint.pubkey(),
            &self.token.pubkey(),
            1,
            &args.authority,
            None,
        )
        .await?;

        let tx = Transaction::new_signed_with_payer(
            &[instruction::create_metadata_accounts_v3(
                id(),
                self.metadata,
                self.mint.pubkey(),
                args.authority.pubkey(),
                context.payer.pubkey(),
                args.authority.pubkey(),
                args.name,
                args.symbol,
                args.uri,
                args.creators,
                args.seller_fee_basis_points,
                false,
                args.is_mutable,
                args.collection,
                args.uses,
                args.collection_details,
            )],
            Some(&args.authority.pubkey()),
            &[&context.payer, &args.authority],
            context.last_blockhash,
        );

        context.banks_client.process_transaction(tx).await
    }

    pub async fn mint_default(
        &mut self,
        context: &mut ProgramTestContext,
        authority: Option<Keypair>,
    ) -> Result<(), BanksClientError> {
        let mut args = MintArgs::default();
        let authority = authority.unwrap_or_else(|| context.payer.dirty_clone());
        args.authority = authority.dirty_clone();

        self.mint(context, args).await.unwrap();

        let master_edition = MasterEditionV2::new(self);
        master_edition
            .create_v3(context, Some(authority), Some(0))
            .await
            .unwrap();

        self.edition = Some(master_edition.pubkey);

        Ok(())
    }

    pub async fn mint_master_with_supply(
        &mut self,
        context: &mut ProgramTestContext,
        authority: Option<Keypair>,
        supply: u64,
    ) -> Result<(), BanksClientError> {
        let mut args = MintArgs::default();
        let authority = authority.unwrap_or_else(|| context.payer.dirty_clone());
        args.authority = authority.dirty_clone();

        self.mint(context, args).await.unwrap();

        let master_edition = MasterEditionV2::new(self);
        master_edition
            .create_v3(context, Some(authority), Some(supply))
            .await
            .unwrap();

        self.edition = Some(master_edition.pubkey);

        Ok(())
    }

    pub async fn set_and_verify_collection(
        &self,
        context: &mut ProgramTestContext,
        args: SetAndVerifyCollectionArgs,
    ) -> Result<(), BanksClientError> {
        let tx = Transaction::new_signed_with_payer(
            &[instruction::set_and_verify_collection(
                id(),
                self.metadata,
                args.collection_authority.pubkey(),
                context.payer.pubkey(),
                args.nft_update_authority,
                args.collection_mint,
                args.collection_metadata,
                args.collection_master_edition_account,
                args.collection_authority_record,
            )],
            Some(&context.payer.pubkey()),
            &[&context.payer, &args.collection_authority],
            context.last_blockhash,
        );
        context.banks_client.process_transaction(tx).await
    }

    pub async fn set_new_update_authority(
        &self,
        context: &mut ProgramTestContext,
        args: SetNewUpdateAuthorityArgs,
    ) -> Result<(), BanksClientError> {
        let mut builder = UpdateBuilder::new();
        builder
            .authority(args.update_authority.pubkey())
            .mint(self.mint.pubkey())
            .metadata(self.metadata)
            .edition(self.edition.unwrap())
            .payer(args.update_authority.pubkey());

        let mut update_args = UpdateArgs::default();
        let UpdateArgs::V1 {
            new_update_authority,
            ..
        } = &mut update_args;
        *new_update_authority = Some(args.new_update_authority);

        let update_ix = builder.build(update_args).unwrap().instruction();

        let tx = Transaction::new_signed_with_payer(
            &[update_ix],
            Some(&args.update_authority.pubkey()),
            &[&args.update_authority],
            context.last_blockhash,
        );
        context.banks_client.process_transaction(tx).await
    }

    pub async fn spl_delegate(
        &self,
        context: &mut ProgramTestContext,
        authority: &Keypair,
        delegate: &Pubkey,
    ) -> Result<(), BanksClientError> {
        let tx = Transaction::new_signed_with_payer(
            &[spl_token::instruction::approve(
                &spl_token::id(),
                &self.token.pubkey(),
                delegate,
                &authority.pubkey(),
                &[],
                1,
            )
            .unwrap()],
            Some(&context.payer.pubkey()),
            &[&context.payer, authority],
            context.last_blockhash,
        );
        context.banks_client.process_transaction(tx).await
    }

    pub async fn freeze_token(
        &self,
        context: &mut ProgramTestContext,
        delegate: &Keypair,
    ) -> Result<(), BanksClientError> {
        let instruction = mpl_token_metadata::instruction::freeze_delegated_account(
            mpl_token_metadata::ID,
            delegate.pubkey(),
            self.token.pubkey(),
            self.edition.unwrap(),
            self.mint.pubkey(),
        );

        let tx = Transaction::new_signed_with_payer(
            &[instruction],
            Some(&delegate.pubkey()),
            &[delegate],
            context.last_blockhash,
        );
        context.banks_client.process_transaction(tx).await
    }

    // Manually injects a frozen state into the NFT's token account.
    pub async fn inject_frozen_state(&self, context: &mut ProgramTestContext) {
        let lamports = context
            .banks_client
            .get_account(self.token.pubkey())
            .await
            .unwrap()
            .unwrap()
            .lamports;

        let account = get_account(context, &self.token.pubkey()).await;
        let mut token_account = spl_token::state::Account::unpack(&account.data).unwrap();
        token_account.state = spl_token::state::AccountState::Frozen;
        let mut data = vec![0; spl_token::state::Account::LEN];
        <spl_token::state::Account as Pack>::pack(token_account, &mut data).unwrap();

        let account = Account {
            lamports,
            data,
            owner: spl_token::ID,
            executable: false,
            rent_epoch: 0,
        };

        context.set_account(&self.token.pubkey(), &account.into())
    }

    pub async fn refresh_accounts(
        &mut self,
        context: &mut ProgramTestContext,
    ) -> Result<(), BanksClientError> {
        let account = get_account(context, &self.token.pubkey()).await;
        let token_account = spl_token::state::Account::unpack(&account.data).unwrap();

        self.token_account = Some(token_account);

        let (token_record_pda, _bump) =
            find_token_record_account(&self.mint.pubkey(), &self.token.pubkey());

        let token_record_account = context
            .banks_client
            .get_account(token_record_pda)
            .await
            .unwrap();

        self.token_record = token_record_account
            .map(|account| TokenRecord::safe_deserialize(&account.data).unwrap());

        Ok(())
    }

    // *** TEST ASSERTIONS ***
    pub async fn assert_pnft_migration(
        &mut self,
        context: &mut ProgramTestContext,
        rule_set: Option<Pubkey>,
        delegate: Option<Pubkey>,
        role: Option<TokenDelegateRole>,
        state: TokenState,
    ) -> Result<(), BanksClientError> {
        self.refresh_accounts(context).await?;

        let md = self.get_data(context).await;

        // Metadata should have the correct token standard.
        assert_eq!(
            md.token_standard,
            Some(TokenStandard::ProgrammableNonFungible)
        );

        // Metadata should have the correct programmable config and rule set.
        let ProgrammableConfig::V1 {
            rule_set: nft_rule_set,
        } = md.programmable_config.unwrap();

        assert_eq!(nft_rule_set, rule_set);

        // Token Account should have 1 token and should be frozen.
        assert_eq!(self.token_account.as_ref().unwrap().amount, 1);
        assert!(self.token_account.as_ref().unwrap().is_frozen());

        // Token Record should exist and have the correct delegate, role and state.
        if let Some(ref record) = self.token_record {
            assert_eq!(record.delegate, delegate);
            assert_eq!(record.delegate_role, role);
            assert_eq!(record.state, state);
        } else {
            panic!("Token record account not found");
        }

        Ok(())
    }
}

impl Default for NfTest {
    fn default() -> Self {
        Self::new()
    }
}

#[derive(Debug)]
pub struct MasterEditionV2 {
    pub pubkey: Pubkey,
    pub metadata_pubkey: Pubkey,
    pub mint_pubkey: Pubkey,
}

impl MasterEditionV2 {
    pub fn new(nft: &NfTest) -> Self {
        let program_id = id();
        let mint_pubkey = nft.mint.pubkey();

        let master_edition_seeds = &[
            PREFIX.as_bytes(),
            program_id.as_ref(),
            mint_pubkey.as_ref(),
            EDITION.as_bytes(),
        ];
        let (pubkey, _) = Pubkey::find_program_address(master_edition_seeds, &id());

        MasterEditionV2 {
            pubkey,
            metadata_pubkey: nft.metadata,
            mint_pubkey,
        }
    }

    pub async fn get_data_from_account(
        context: &mut ProgramTestContext,
        pubkey: &Pubkey,
    ) -> mpl_token_metadata::state::MasterEditionV2 {
        let account = get_account(context, pubkey).await;
        try_from_slice_unchecked(&account.data).unwrap()
    }

    pub async fn create_v3(
        &self,
        context: &mut ProgramTestContext,
        authority: Option<Keypair>,
        max_supply: Option<u64>,
    ) -> Result<(), BanksClientError> {
        let authority = if let Some(auth) = authority {
            auth
        } else {
            context.payer.dirty_clone()
        };

        let tx = Transaction::new_signed_with_payer(
            &[instruction::create_master_edition_v3(
                id(),
                self.pubkey,
                self.mint_pubkey,
                authority.pubkey(),
                authority.pubkey(),
                self.metadata_pubkey,
                authority.pubkey(),
                max_supply,
            )],
            Some(&authority.pubkey()),
            &[&authority],
            context.last_blockhash,
        );

        context.banks_client.process_transaction(tx).await
    }
}


