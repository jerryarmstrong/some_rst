testsuite/src/services_impl/validator/rpc_request.rs
====================================================

Last edited: 2021-03-14 22:40:05

Contents:

.. code-block:: rs

    use std::fmt;

use serde_json::{Value, json};

/*
NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
This entire file is copied from https://github.com/solana-labs/solana/blob/master/client/src/rpc_request.rs
because solana-client provides Ledger support, which means it has a dependency
on the 'hidapi' kernel module. This module won't compile under Docker-for-Mac
due to https://github.com/docker/for-mac/issues/5295
Therefore, we reimplement parts of the Solana client here as a hackaround
NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
*/

pub enum RpcRequest {
    DeregisterNode,
    ValidatorExit,
    GetAccountInfo,
    GetBalance,
    GetBlockTime,
    GetClusterNodes,
    GetConfirmedBlock,
    GetConfirmedBlocks,
    GetConfirmedBlocksWithLimit,
    GetConfirmedSignaturesForAddress,
    GetConfirmedSignaturesForAddress2,
    GetConfirmedTransaction,
    GetEpochInfo,
    GetEpochSchedule,
    GetFeeCalculatorForBlockhash,
    GetFeeRateGovernor,
    GetFees,
    GetFirstAvailableBlock,
    GetGenesisHash,
    GetHealth,
    GetIdentity,
    GetInflationGovernor,
    GetInflationRate,
    GetLargestAccounts,
    GetLeaderSchedule,
    GetMinimumBalanceForRentExemption,
    GetMultipleAccounts,
    GetProgramAccounts,
    GetRecentBlockhash,
    GetSnapshotSlot,
    GetSignatureStatuses,
    GetSlot,
    GetSlotLeader,
    GetStorageTurn,
    GetStorageTurnRate,
    GetSlotsPerSegment,
    GetStoragePubkeysForSlot,
    GetSupply,
    GetTokenAccountBalance,
    GetTokenAccountsByDelegate,
    GetTokenAccountsByOwner,
    GetTokenSupply,
    GetTotalSupply,
    GetTransactionCount,
    GetVersion,
    GetVoteAccounts,
    MinimumLedgerSlot,
    RegisterNode,
    RequestAirdrop,
    SendTransaction,
    SimulateTransaction,
    SignVote,
}

impl fmt::Display for RpcRequest {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let method = match self {
            RpcRequest::DeregisterNode => "deregisterNode",
            RpcRequest::ValidatorExit => "validatorExit",
            RpcRequest::GetAccountInfo => "getAccountInfo",
            RpcRequest::GetBalance => "getBalance",
            RpcRequest::GetBlockTime => "getBlockTime",
            RpcRequest::GetClusterNodes => "getClusterNodes",
            RpcRequest::GetConfirmedBlock => "getConfirmedBlock",
            RpcRequest::GetConfirmedBlocks => "getConfirmedBlocks",
            RpcRequest::GetConfirmedBlocksWithLimit => "getConfirmedBlocksWithLimit",
            RpcRequest::GetConfirmedSignaturesForAddress => "getConfirmedSignaturesForAddress",
            RpcRequest::GetConfirmedSignaturesForAddress2 => "getConfirmedSignaturesForAddress2",
            RpcRequest::GetConfirmedTransaction => "getConfirmedTransaction",
            RpcRequest::GetEpochInfo => "getEpochInfo",
            RpcRequest::GetEpochSchedule => "getEpochSchedule",
            RpcRequest::GetFeeCalculatorForBlockhash => "getFeeCalculatorForBlockhash",
            RpcRequest::GetFeeRateGovernor => "getFeeRateGovernor",
            RpcRequest::GetFees => "getFees",
            RpcRequest::GetFirstAvailableBlock => "getFirstAvailableBlock",
            RpcRequest::GetGenesisHash => "getGenesisHash",
            RpcRequest::GetHealth => "getHealth",
            RpcRequest::GetIdentity => "getIdentity",
            RpcRequest::GetInflationGovernor => "getInflationGovernor",
            RpcRequest::GetInflationRate => "getInflationRate",
            RpcRequest::GetLargestAccounts => "getLargestAccounts",
            RpcRequest::GetLeaderSchedule => "getLeaderSchedule",
            RpcRequest::GetMinimumBalanceForRentExemption => "getMinimumBalanceForRentExemption",
            RpcRequest::GetMultipleAccounts => "getMultipleAccounts",
            RpcRequest::GetProgramAccounts => "getProgramAccounts",
            RpcRequest::GetRecentBlockhash => "getRecentBlockhash",
            RpcRequest::GetSnapshotSlot => "getSnapshotSlot",
            RpcRequest::GetSignatureStatuses => "getSignatureStatuses",
            RpcRequest::GetSlot => "getSlot",
            RpcRequest::GetSlotLeader => "getSlotLeader",
            RpcRequest::GetStorageTurn => "getStorageTurn",
            RpcRequest::GetStorageTurnRate => "getStorageTurnRate",
            RpcRequest::GetSlotsPerSegment => "getSlotsPerSegment",
            RpcRequest::GetStoragePubkeysForSlot => "getStoragePubkeysForSlot",
            RpcRequest::GetSupply => "getSupply",
            RpcRequest::GetTokenAccountBalance => "getTokenAccountBalance",
            RpcRequest::GetTokenAccountsByDelegate => "getTokenAccountsByDelegate",
            RpcRequest::GetTokenAccountsByOwner => "getTokenAccountsByOwner",
            RpcRequest::GetTokenSupply => "getTokenSupply",
            RpcRequest::GetTotalSupply => "getTotalSupply",
            RpcRequest::GetTransactionCount => "getTransactionCount",
            RpcRequest::GetVersion => "getVersion",
            RpcRequest::GetVoteAccounts => "getVoteAccounts",
            RpcRequest::MinimumLedgerSlot => "minimumLedgerSlot",
            RpcRequest::RegisterNode => "registerNode",
            RpcRequest::RequestAirdrop => "requestAirdrop",
            RpcRequest::SendTransaction => "sendTransaction",
            RpcRequest::SimulateTransaction => "simulateTransaction",
            RpcRequest::SignVote => "signVote",
        };

        write!(f, "{}", method)
    }
}

pub const MAX_GET_SIGNATURE_STATUSES_QUERY_ITEMS: usize = 256;
pub const MAX_GET_CONFIRMED_SIGNATURES_FOR_ADDRESS_SLOT_RANGE: u64 = 10_000;
pub const MAX_GET_CONFIRMED_BLOCKS_RANGE: u64 = 500_000;
pub const MAX_GET_CONFIRMED_SIGNATURES_FOR_ADDRESS2_LIMIT: usize = 1_000;
pub const MAX_MULTIPLE_ACCOUNTS: usize = 100;
pub const NUM_LARGEST_ACCOUNTS: usize = 20;
pub const MAX_GET_PROGRAM_ACCOUNT_FILTERS: usize = 4;

// Validators that are this number of slots behind are considered delinquent
pub const DELINQUENT_VALIDATOR_SLOT_DISTANCE: u64 = 128;

impl RpcRequest {
    pub(crate) fn build_request_json(self, id: u64, params: Value) -> Value {
        let jsonrpc = "2.0";
        json!({
           "jsonrpc": jsonrpc,
           "id": id,
           "method": format!("{}", self),
           "params": params,
        })
    }
}

