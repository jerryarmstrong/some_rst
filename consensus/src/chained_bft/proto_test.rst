consensus/src/chained_bft/proto_test.rs
=======================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use crate::chained_bft::{
    consensus_types::{
        block::Block,
        proposal_msg::{ProposalMsg, ProposalUncheckedSignatures},
        quorum_cert::QuorumCert,
        sync_info::SyncInfo,
        vote_data::VoteData,
        vote_msg::VoteMsg,
    },
    test_utils::placeholder_ledger_info,
};
use prost::Message;
use solana_libra_crypto::HashValue;
use solana_libra_executor::ExecutedState;
use solana_libra_prost_ext::MessageExt;
use solana_libra_types::validator_signer::ValidatorSigner;
use std::convert::{TryFrom, TryInto};

#[test]
fn test_proto_convert_block() {
    let block: Block<u64> = Block::make_genesis_block();
    let block_proto = solana_libra_network::proto::Block::from(block.clone());
    assert_eq!(block, block_proto.try_into().unwrap());
}

#[test]
fn test_proto_convert_proposal() {
    let genesis_qc = QuorumCert::certificate_for_genesis();
    let proposal = ProposalMsg::new(
        Block::<u64>::make_genesis_block(),
        SyncInfo::new(genesis_qc.clone(), genesis_qc.clone(), None),
    );
    //
    let protoed: solana_libra_network::proto::Proposal = proposal.clone().into();
    let unprotoed: ProposalMsg<u64> = ProposalUncheckedSignatures::<u64>::try_from(protoed)
        .expect("Should convert.")
        .into();
    assert_eq!(proposal, unprotoed);
    //
    let protoed = solana_libra_network::proto::Proposal::from(proposal.clone())
        .to_bytes()
        .unwrap();
    let unprotoed: ProposalMsg<u64> = ProposalUncheckedSignatures::<u64>::try_from(
        solana_libra_network::proto::Proposal::decode(protoed).unwrap(),
    )
    .expect("Should convert.")
    .into();
    assert_eq!(proposal, unprotoed);
}

#[test]
fn test_proto_convert_vote() {
    let signer = ValidatorSigner::random(None);
    let vote = VoteMsg::new(
        VoteData::new(
            HashValue::random(),
            ExecutedState::state_for_genesis().state_id,
            1,
            HashValue::random(),
            0,
            HashValue::random(),
            0,
        ),
        signer.author(),
        placeholder_ledger_info(),
        &signer,
    );
    let vote_proto = solana_libra_network::proto::Vote::from(vote.clone());
    assert_eq!(vote, vote_proto.try_into().unwrap());
}


