cNft-Governance/governance-program-library/programs/cnft-voter/tests/program_test/cnft_voter_test.rs
====================================================================================================

Last edited: 2023-07-14 15:51:14

Contents:

.. code-block:: rs

    use crate::program_test::governance_test::{
    GovernanceTest, ProposalCookie, RealmCookie, TokenOwnerRecordCookie,
};
use crate::program_test::merkle_tree_test::{LeafArgs, MerkleTreeCookie, MerkleTreeTest};
use crate::program_test::program_test_bench::ProgramTestBench;
use crate::program_test::program_test_bench::WalletCookie;
use crate::program_test::token_metadata_test::{NftCollectionCookie, TokenMetadataTest};
use crate::program_test::tools::NopOverride;
use anchor_lang::prelude::Pubkey;
use gpl_cnft_voter::state::get_cnft_vote_record_address;
use gpl_cnft_voter::state::max_voter_weight_record::{
    get_max_voter_weight_record_address, MaxVoterWeightRecord,
};
use gpl_cnft_voter::state::*;
use gpl_cnft_voter::state::CompressedNftAsset as LeafVerificationCookie;
use solana_program::instruction::AccountMeta;
use solana_program_test::{BanksClientError, ProgramTest};
use solana_sdk::instruction::Instruction;
use solana_sdk::signature::Keypair;
use solana_sdk::signer::Signer;
use spl_governance::state::vote_record;
use spl_governance::{
    instruction::cast_vote,
    state::vote_record::{Vote, VoteChoice},
};
use std::sync::Arc;

#[derive(Debug, PartialEq)]
pub struct RegistrarCookie {
    pub address: Pubkey,
    pub account: Registrar,

    pub realm_authority: Keypair,
    pub max_collections: u8,
}

pub struct VoterWeightRecordCookie {
    pub address: Pubkey,
    pub account: VoterWeightRecord,
}

pub struct MaxVoterWeightRecordCookie {
    pub address: Pubkey,
    pub account: MaxVoterWeightRecord,
}

pub struct CollectionConfigCookie {
    pub collection_config: CollectionConfig,
}

pub struct ConfigureCollectionArgs {
    pub weight: u64,
    pub size: u32,
}

impl Default for ConfigureCollectionArgs {
    fn default() -> Self {
        Self { weight: 1, size: 3 }
    }
}

#[derive(Debug, PartialEq)]
pub struct CompressedNftVoteRecordCookie {
    pub address: Pubkey,
    pub account: CompressedNftVoteRecord,
}

pub struct CastCompressedNftVoteArgs {
    pub cast_spl_gov_vote: bool,
}

impl Default for CastCompressedNftVoteArgs {
    fn default() -> Self {
        Self {
            cast_spl_gov_vote: true,
        }
    }
}

pub struct CompressedNftVoterTest {
    pub program_id: Pubkey,
    pub bench: Arc<ProgramTestBench>,
    pub governance: GovernanceTest,
    pub token_metadata: TokenMetadataTest,
    pub merkle_tree: MerkleTreeTest,
}

impl CompressedNftVoterTest {
    #[allow(dead_code)]
    pub fn add_program(program_test: &mut ProgramTest) {
        program_test.add_program("gpl_cnft_voter", gpl_cnft_voter::id(), None);
    }

    #[allow(dead_code)]
    pub async fn start_new() -> Self {
        // println!("Starting new test");
        let mut program_test = ProgramTest::default();

        CompressedNftVoterTest::add_program(&mut program_test);
        GovernanceTest::add_program(&mut program_test);
        TokenMetadataTest::add_program(&mut program_test);
        MerkleTreeTest::add_program(&mut program_test);

        let program_id = gpl_cnft_voter::id();
        println!("Program ID: {}", program_id);

        let bench = ProgramTestBench::start_new(program_test).await;
        let bench_rc = Arc::new(bench);

        let governance_bench =
            GovernanceTest::new(bench_rc.clone(), Some(program_id), Some(program_id));
        let token_metadata_bench = TokenMetadataTest::new(bench_rc.clone());
        let merkle_tree_bench = MerkleTreeTest::new(bench_rc.clone());

        Self {
            program_id,
            bench: bench_rc,
            governance: governance_bench,
            token_metadata: token_metadata_bench,
            merkle_tree: merkle_tree_bench,
        }
    }

    #[allow(dead_code)]
    pub async fn with_registrar(
        &mut self,
        realm_cookie: &RealmCookie,
    ) -> Result<RegistrarCookie, BanksClientError> {
        self.with_registrar_using_ix(realm_cookie, NopOverride, None)
            .await
    }

    #[allow(dead_code)]
    pub async fn with_registrar_using_ix<F: Fn(&mut Instruction)>(
        &mut self,
        realm_cookie: &RealmCookie,
        instruction_override: F,
        signers_override: Option<&[&Keypair]>,
    ) -> Result<RegistrarCookie, BanksClientError> {
        let registrar_key =
            get_registrar_address(&realm_cookie.address, &realm_cookie.account.community_mint);
        let max_collections = 10;
        let data =
            anchor_lang::InstructionData::data(&gpl_cnft_voter::instruction::CreateRegistrar {
                max_collections,
            });

        let accounts = anchor_lang::ToAccountMetas::to_account_metas(
            &gpl_cnft_voter::accounts::CreateRegistrar {
                registrar: registrar_key,
                realm: realm_cookie.address,
                governance_program_id: self.governance.program_id,
                governing_token_mint: realm_cookie.account.community_mint,
                realm_authority: realm_cookie.get_realm_authority().pubkey(),
                payer: self.bench.payer.pubkey(),
                system_program: anchor_lang::solana_program::system_program::id(),
            },
            None,
        );

        let mut create_registrar_ix = Instruction {
            program_id: gpl_cnft_voter::id(),
            accounts,
            data,
        };

        instruction_override(&mut create_registrar_ix);

        let default_signers = &[&realm_cookie.realm_authority];
        let signers = signers_override.unwrap_or(default_signers);

        self.bench
            .process_transaction(&[create_registrar_ix], Some(signers))
            .await?;

        let account = Registrar {
            governance_program_id: self.governance.program_id,
            realm: realm_cookie.address,
            governing_token_mint: realm_cookie.account.community_mint,
            collection_configs: vec![],
            reserved: [0; 128],
        };

        Ok(RegistrarCookie {
            address: registrar_key,
            account,
            realm_authority: realm_cookie.get_realm_authority(),
            max_collections,
        })
    }

    #[allow(dead_code)]
    pub async fn get_registrar_account(&mut self, registrar: &Pubkey) -> Registrar {
        self.bench.get_anchor_account::<Registrar>(*registrar).await
    }

    #[allow(dead_code)]
    pub async fn with_max_voter_weight_record(
        &mut self,
        registrar_cookie: &RegistrarCookie,
    ) -> Result<MaxVoterWeightRecordCookie, BanksClientError> {
        self.with_max_voter_weight_record_using_ix(registrar_cookie, NopOverride)
            .await
    }

    #[allow(dead_code)]
    pub async fn with_max_voter_weight_record_using_ix<F: Fn(&mut Instruction)>(
        &mut self,
        registrar_cookie: &RegistrarCookie,
        instruction_override: F,
    ) -> Result<MaxVoterWeightRecordCookie, BanksClientError> {
        let max_voter_weight_record_key = get_max_voter_weight_record_address(
            &registrar_cookie.account.realm,
            &registrar_cookie.account.governing_token_mint,
        );

        let data = anchor_lang::InstructionData::data(
            &gpl_cnft_voter::instruction::CreateMaxVoterWeightRecord {},
        );

        let accounts = gpl_cnft_voter::accounts::CreateMaxVoterWeightRecord {
            max_voter_weight_record: max_voter_weight_record_key,
            governance_program_id: self.governance.program_id,
            realm: registrar_cookie.account.realm,
            realm_governing_token_mint: registrar_cookie.account.governing_token_mint,
            payer: self.bench.payer.pubkey(),
            system_program: solana_sdk::system_program::id(),
        };

        let mut create_max_voter_weight_record_ix = Instruction {
            program_id: gpl_cnft_voter::id(),
            accounts: anchor_lang::ToAccountMetas::to_account_metas(&accounts, None),
            data,
        };

        instruction_override(&mut create_max_voter_weight_record_ix);

        self.bench
            .process_transaction(&[create_max_voter_weight_record_ix], None)
            .await?;

        let account = MaxVoterWeightRecord {
            realm: registrar_cookie.account.realm,
            governing_token_mint: registrar_cookie.account.governing_token_mint,
            max_voter_weight: 0,
            max_voter_weight_expiry: Some(0),
            reserved: [0; 8],
        };

        Ok(MaxVoterWeightRecordCookie {
            account,
            address: max_voter_weight_record_key,
        })
    }

    #[allow(dead_code)]
    pub async fn get_max_voter_weight_record(
        &self,
        max_voter_weight_record: &Pubkey,
    ) -> MaxVoterWeightRecord {
        self.bench
            .get_anchor_account(*max_voter_weight_record)
            .await
    }

    #[allow(dead_code)]
    pub async fn with_voter_weight_record(
        &mut self,
        registrar_cookie: &RegistrarCookie,
        voter_cookie: &WalletCookie,
    ) -> Result<VoterWeightRecordCookie, BanksClientError> {
        self.with_voter_weight_record_using_ix(registrar_cookie, voter_cookie, NopOverride)
            .await
    }

    #[allow(dead_code)]
    pub async fn with_voter_weight_record_using_ix<F: Fn(&mut Instruction)>(
        &mut self,
        registrar_cookie: &RegistrarCookie,
        voter_cookie: &WalletCookie,
        instruction_override: F,
    ) -> Result<VoterWeightRecordCookie, BanksClientError> {
        let governing_token_owner = voter_cookie.address;

        let (voter_weight_record_key, _) = Pubkey::find_program_address(
            &[
                b"voter-weight-record".as_ref(),
                registrar_cookie.account.realm.as_ref(),
                registrar_cookie.account.governing_token_mint.as_ref(),
                governing_token_owner.as_ref(),
            ],
            &gpl_cnft_voter::id(),
        );

        let data = anchor_lang::InstructionData::data(
            &gpl_cnft_voter::instruction::CreateVoterWeightRecord {
                governing_token_owner,
            },
        );

        let accounts = gpl_cnft_voter::accounts::CreateVoterWeightRecord {
            voter_weight_record: voter_weight_record_key,
            governance_program_id: self.governance.program_id,
            realm: registrar_cookie.account.realm,
            realm_governing_token_mint: registrar_cookie.account.governing_token_mint,
            payer: self.bench.payer.pubkey(),
            system_program: solana_sdk::system_program::id(),
        };

        let mut create_voter_weight_record_ix = Instruction {
            program_id: gpl_cnft_voter::id(),
            accounts: anchor_lang::ToAccountMetas::to_account_metas(&accounts, None),
            data,
        };

        instruction_override(&mut create_voter_weight_record_ix);

        self.bench
            .process_transaction(&[create_voter_weight_record_ix], None)
            .await?;

        let account = VoterWeightRecord {
            realm: registrar_cookie.account.realm,
            governing_token_mint: registrar_cookie.account.governing_token_mint,
            governing_token_owner,
            voter_weight: 0,
            voter_weight_expiry: Some(0),
            weight_action: None,
            weight_action_target: None,
            reserved: [0; 8],
        };

        Ok(VoterWeightRecordCookie {
            address: voter_weight_record_key,
            account,
        })
    }

    #[allow(dead_code)]
    pub async fn get_voter_weight_record(&self, voter_weight_record: &Pubkey) -> VoterWeightRecord {
        self.bench.get_anchor_account(*voter_weight_record).await
    }

    #[allow(dead_code)]
    pub async fn with_collection(
        &mut self,
        registrar_cookie: &RegistrarCookie,
        nft_collection_cookie: &NftCollectionCookie,
        max_voter_weight_record_cookie: &MaxVoterWeightRecordCookie,
        args: Option<ConfigureCollectionArgs>,
    ) -> Result<CollectionConfigCookie, BanksClientError> {
        self.with_collection_using_ix(
            registrar_cookie,
            nft_collection_cookie,
            max_voter_weight_record_cookie,
            args,
            NopOverride,
            None,
        )
        .await
    }

    #[allow(dead_code)]
    pub async fn with_collection_using_ix<F: Fn(&mut Instruction)>(
        &mut self,
        registrar_cookie: &RegistrarCookie,
        nft_collection_cookie: &NftCollectionCookie,
        max_voter_weight_record_cookie: &MaxVoterWeightRecordCookie,
        args: Option<ConfigureCollectionArgs>,
        instruction_override: F,
        signers_override: Option<&[&Keypair]>,
    ) -> Result<CollectionConfigCookie, BanksClientError> {
        let args = args.unwrap_or_default();

        let data =
            anchor_lang::InstructionData::data(&gpl_cnft_voter::instruction::ConfigureCollection {
                weight: args.weight,
                size: args.size,
            });

        let accounts = gpl_cnft_voter::accounts::ConfigureCollection {
            registrar: registrar_cookie.address,
            realm: registrar_cookie.account.realm,
            realm_authority: registrar_cookie.realm_authority.pubkey(),
            collection: nft_collection_cookie.mint,
            max_voter_weight_record: max_voter_weight_record_cookie.address,
        };

        let mut configure_collection_ix = Instruction {
            program_id: gpl_cnft_voter::id(),
            accounts: anchor_lang::ToAccountMetas::to_account_metas(&accounts, None),
            data,
        };

        instruction_override(&mut configure_collection_ix);

        let default_signers = &[&registrar_cookie.realm_authority];
        let signers = signers_override.unwrap_or(default_signers);

        self.bench
            .process_transaction(&[configure_collection_ix], Some(signers))
            .await?;

        let collection_config = CollectionConfig {
            collection: nft_collection_cookie.mint,
            size: args.size,
            weight: args.weight,
            reserved: [0; 8],
        };

        Ok(CollectionConfigCookie { collection_config })
    }

    #[allow(dead_code)]
    pub async fn with_cnft_verification(
        &mut self,
        voter_cookie: &WalletCookie,
        merkle_tree_cookie: &mut MerkleTreeCookie,
        leaf_cookie: &LeafArgs,
        leaf_verification_cookie: &LeafVerificationCookie,
        proofs: &Vec<AccountMeta>,
    ) -> Result<(), BanksClientError> {
        self.with_cnft_verification_using_ix(
            voter_cookie,
            merkle_tree_cookie,
            leaf_cookie,
            leaf_verification_cookie,
            &proofs,
            NopOverride,
            None,
        )
        .await
    }

    #[allow(dead_code)]
    pub async fn with_cnft_verification_using_ix<F: Fn(&mut Instruction)>(
        &mut self,
        voter_cookie: &WalletCookie,
        tree_cookie: &mut MerkleTreeCookie,
        leaf_cookie: &LeafArgs,
        leaf_verification_cookie: &LeafVerificationCookie,
        proofs: &Vec<AccountMeta>,
        instruction_override: F,
        signers_override: Option<&[&Keypair]>,
    ) -> Result<(), BanksClientError> {
        // let tree_authority = &tree_cookie.tree_authority;
        let proofs = &mut proofs.clone();

        let accounts = gpl_cnft_voter::accounts::VerifyCompressedNftInfo {
            // tree_authority: *tree_authority,
            leaf_owner: leaf_cookie.owner.pubkey(),
            leaf_delegate: leaf_cookie.delegate.pubkey(),
            merkle_tree: tree_cookie.address,
            // payer: self.bench.payer.pubkey(),
            payer: leaf_cookie.owner.pubkey(),
            compression_program: spl_account_compression::id(),
            system_program: solana_sdk::system_program::id(),
        };

        let data = anchor_lang::InstructionData::data(
            &gpl_cnft_voter::instruction::VerifyCompressedNftInfo {
                params: leaf_verification_cookie.clone(),
            },
        );

        let mut verify_cnft_info_ix = Instruction {
            program_id: gpl_cnft_voter::id(),
            accounts: anchor_lang::ToAccountMetas::to_account_metas(&accounts, None),
            data,
        };

        verify_cnft_info_ix.accounts.append(proofs);

        instruction_override(&mut verify_cnft_info_ix);
        // println!("{:?}", &self.bench.payer.pubkey());
        // println!("{:?}", &leaf_cookie.owner.pubkey());
        // println!("{:?}", &leaf_cookie.delegate.pubkey());
        let default_signers = &[
            &leaf_cookie.owner,
            &leaf_cookie.delegate,
            &voter_cookie.signer,
        ];
        let signers = signers_override.unwrap_or(default_signers);

        self.bench
            .process_transaction(&[verify_cnft_info_ix], Some(signers))
            .await?;

        Ok(())
    }

    #[allow(dead_code)]
    pub async fn cast_cnft_vote(
        &mut self,
        registrar_cookie: &RegistrarCookie,
        voter_weight_record_cookie: &VoterWeightRecordCookie,
        voter_token_owner_record_cookie: &TokenOwnerRecordCookie,
        max_voter_weight_record_cookie: &MaxVoterWeightRecordCookie,
        proposal_cookie: &ProposalCookie,
        voter_cookie: &WalletCookie,
        // nft_collection_cookie: &NftCollectionCookie,
        tree_cookie: &MerkleTreeCookie,
        leaf_cookies: &[&LeafArgs],
        leaf_verification_cookies: &[&LeafVerificationCookie],
        proofs: &[&Vec<AccountMeta>],
        args: Option<CastCompressedNftVoteArgs>,
    ) -> Result<Vec<CompressedNftVoteRecordCookie>, BanksClientError> {
        let args = args.unwrap_or_default();
        let params: Vec<LeafVerificationCookie> = leaf_verification_cookies
            .to_vec()
            .into_iter()
            .map(|v| v.clone())
            .collect();
        let data = anchor_lang::InstructionData::data(
            &gpl_cnft_voter::instruction::CastCompressedNftVote {
                proposal: proposal_cookie.address,
                params: params.to_vec(),
            },
        );

        let accounts = gpl_cnft_voter::accounts::CastCompressedNftVote {
            registrar: registrar_cookie.address,
            voter_weight_record: voter_weight_record_cookie.address,
            voter_token_owner_record: voter_token_owner_record_cookie.address,
            voter_authority: voter_cookie.address,
            // collection_mint: nft_collection_cookie.mint,
            merkle_tree: tree_cookie.address,
            leaf_owner: leaf_cookies[0].owner.pubkey(),
            leaf_delegate: leaf_cookies[0].delegate.pubkey(),
            payer: self.bench.payer.pubkey(),
            compression_program: spl_account_compression::id(),
            system_program: solana_sdk::system_program::id(),
        };

        let mut cast_cnft_vote_ix = Instruction {
            program_id: gpl_cnft_voter::id(),
            accounts: anchor_lang::ToAccountMetas::to_account_metas(&accounts, None),
            data,
        };
        let mut cnft_vote_record_cookies = vec![];

        for i in 0..leaf_verification_cookies.len() {
            let cnft_voter_record_key = get_cnft_vote_record_address(
                &proposal_cookie.address,
                &leaf_verification_cookies[i].asset_id,
            );
            let cnft_vote_record_info = AccountMeta::new(cnft_voter_record_key, false);
            let proof = &mut proofs[i].clone();
            cast_cnft_vote_ix.accounts.append(proof);
            cast_cnft_vote_ix.accounts.push(cnft_vote_record_info);

            let account = CompressedNftVoteRecord {
                proposal: proposal_cookie.address,
                asset_id: leaf_verification_cookies[i].asset_id,
                governing_token_owner: voter_weight_record_cookie.account.governing_token_owner,
                account_discriminator: CompressedNftVoteRecord::ACCOUNT_DISCRIMINATOR,
                reserved: [0; 8],
            };
            cnft_vote_record_cookies.push(CompressedNftVoteRecordCookie {
                address: cnft_voter_record_key,
                account,
            });
        }

        let mut instructions = vec![cast_cnft_vote_ix];
        if args.cast_spl_gov_vote {
            // spl-gov cast vote
            let vote = Vote::Approve(vec![VoteChoice {
                rank: 0,
                weight_percentage: 100,
            }]);

            let cast_vote_ix = cast_vote(
                &self.governance.program_id,
                &registrar_cookie.account.realm,
                &proposal_cookie.account.governance,
                &proposal_cookie.address,
                &proposal_cookie.account.token_owner_record,
                &voter_token_owner_record_cookie.address,
                &voter_cookie.address,
                &proposal_cookie.account.governing_token_mint,
                &self.bench.payer.pubkey(),
                Some(voter_weight_record_cookie.address),
                Some(max_voter_weight_record_cookie.address),
                vote,
            );

            instructions.push(cast_vote_ix);
        }

        let signers = &[&voter_cookie.signer];
        self.bench
            .process_transaction(&instructions, Some(signers))
            .await?;

        Ok(cnft_vote_record_cookies)
    }

    #[allow(dead_code)]
    pub async fn update_voter_weight_record(
        &self,
        registrar_cookie: &RegistrarCookie,
        voter_weight_record_cookie: &VoterWeightRecordCookie,
        voter_weight_action: VoterWeightAction,
        // nft_collection_cookie: &NftCollectionCookie,
        tree_cookie: &MerkleTreeCookie,
        leaf_cookies: &[&LeafArgs],
        leaf_verification_cookies: &[&LeafVerificationCookie],
        proofs: &[&Vec<AccountMeta>],
    ) -> Result<(), BanksClientError> {
        let params: Vec<LeafVerificationCookie> = leaf_verification_cookies
            .to_vec()
            .into_iter()
            .map(|v| v.clone())
            .collect();
        let data = anchor_lang::InstructionData::data(
            &gpl_cnft_voter::instruction::UpdateVoterWeightRecord {
                voter_weight_action: voter_weight_action.into(),
                params,
            },
        );

        let accounts = gpl_cnft_voter::accounts::UpdateVoterWeightRecord {
            registrar: registrar_cookie.address,
            voter_weight_record: voter_weight_record_cookie.address,
            // collection_mint: nft_collection_cookie.mint,
            merkle_tree: tree_cookie.address,
            leaf_owner: leaf_cookies[0].owner.pubkey(),
            leaf_delegate: leaf_cookies[0].delegate.pubkey(),
            compression_program: spl_account_compression::id(),
        };

        let mut update_voter_weight_record_ix = Instruction {
            program_id: gpl_cnft_voter::id(),
            accounts: anchor_lang::ToAccountMetas::to_account_metas(&accounts, None),
            data,
        };

        for i in 0..leaf_verification_cookies.len() {
            let proof = &mut proofs[i].clone();
            update_voter_weight_record_ix.accounts.append(proof);
        }

        self.bench
            .process_transaction(&[update_voter_weight_record_ix], None)
            .await
    }

    #[allow(dead_code)]
    pub async fn relinquish_cnft_vote(
        &self,
        registrar_cookie: &RegistrarCookie,
        voter_weight_record_cookie: &VoterWeightRecordCookie,
        proposal_cookie: &ProposalCookie,
        voter_cookie: &WalletCookie,
        voter_token_owner_record_cookie: &TokenOwnerRecordCookie,
        cnft_vote_record_cookies: &Vec<CompressedNftVoteRecordCookie>,
    ) -> Result<(), BanksClientError> {
        let data = anchor_lang::InstructionData::data(
            &gpl_cnft_voter::instruction::RelinquishCompressedNftVote {},
        );

        let vote_record_key = vote_record::get_vote_record_address(
            &self.governance.program_id,
            &proposal_cookie.address,
            &voter_token_owner_record_cookie.address,
        );

        let accounts = gpl_cnft_voter::accounts::RelinquishCompressedNftVote {
            registrar: registrar_cookie.address,
            voter_weight_record: voter_weight_record_cookie.address,
            governance: proposal_cookie.account.governance,
            proposal: proposal_cookie.address,
            vote_record: vote_record_key,
            beneficiary: voter_cookie.address, // why not voter
            voter_token_owner_record: voter_token_owner_record_cookie.address,
            voter_authority: voter_cookie.address,
        };

        let mut relinquish_cnft_vote_ix = Instruction {
            program_id: gpl_cnft_voter::id(),
            accounts: anchor_lang::ToAccountMetas::to_account_metas(&accounts, None),
            data,
        };

        for cnft_vote_record_cookie in cnft_vote_record_cookies {
            relinquish_cnft_vote_ix
                .accounts
                .push(AccountMeta::new(cnft_vote_record_cookie.address, false));
        }

        let signers = &[&voter_cookie.signer];
        self.bench
            .process_transaction(&[relinquish_cnft_vote_ix], Some(signers))
            .await?;
        Ok(())
    }

    #[allow(dead_code)]
    pub async fn get_cnft_vote_record_account(
        &mut self,
        cnft_vote_record: &Pubkey,
    ) -> CompressedNftVoteRecord {
        self.bench
            .get_borsh_account::<CompressedNftVoteRecord>(cnft_vote_record)
            .await
    }
}


