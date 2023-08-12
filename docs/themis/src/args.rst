src/args.rs
===========

Last edited: 2023-07-17 22:54:02

Contents:

.. code-block:: rs

    use std::path::PathBuf;

use clap::{Parser, Subcommand};
use solana_program::pubkey::Pubkey;

use crate::{processor::MintType, Vote};

#[derive(Parser)]
#[clap(author, version, about)]
pub struct Args {
    /// Path to the keypair file.
    #[arg(short, long, global = true)]
    pub keypair_path: Option<PathBuf>,

    /// RPC URL for the Solana cluster.
    #[arg(short, long, global = true)]
    pub rpc_url: Option<String>,

    #[clap(subcommand)]
    pub command: Commands,
}

#[derive(Clone, Subcommand)]
pub enum Commands {
    /// Create a proposal for upgrading a program
    UpgradeProgram {
        /// Proposal name
        #[arg(short = 'b', long)]
        source_buffer: Pubkey,

        /// Account to return buffer funds to, defaults to authority keypair
        #[arg(short, long)]
        spill_account: Option<Pubkey>,

        /// Proposal name
        #[arg(short, long)]
        name: String,

        /// Proposal description or link to proposal description
        #[arg(short, long)]
        description: String,

        /// Mint type: Member or Council
        #[arg(short, long, default_value = "council")]
        mint_type: MintType,

        #[arg(short, long)]
        options: Vec<String>,
    },
    /// Vote on a proposal
    Vote {
        /// Vote: true = yes, false = no
        vote_choice: Vote,

        /// Proposal pubkey
        #[arg(short, long)]
        proposal_id: Option<Pubkey>,

        /// Vote on the most recent proposal
        #[arg(short, long)]
        latest: bool,

        #[arg(short, long, default_value = "council")]
        mint_type: MintType,
    },
    /// Execute a proposal
    Execute {
        /// Proposal pubkey
        #[arg(short, long)]
        proposal_id: Option<Pubkey>,

        /// Vote on the most recent proposal
        #[arg(short, long)]
        latest: bool,

        #[arg(short, long, default_value = "council")]
        mint_type: MintType,
    },
    /// Cancel a proposal
    Cancel {
        /// Proposal pubkey
        #[arg(short, long)]
        proposal_id: Option<Pubkey>,

        /// Vote on the most recent proposal
        #[arg(short, long)]
        latest: bool,

        #[arg(short, long, default_value = "council")]
        mint_type: MintType,
    },
    /// Deposit governance tokens
    Deposit {
        /// Amount of governance tokens to deposit
        amount: u64,

        #[arg(short, long, default_value = "council")]
        mint_type: MintType,
    },
    /// Withdraw governance tokens
    Withdraw {
        #[arg(short, long, default_value = "council")]
        mint_type: MintType,
    },
    /// Update a governance configuration
    UpdateConfig {
        /// Mint type: Member or Council
        #[arg(short, long, default_value = "council")]
        mint_type: MintType,

        #[arg(long)]
        vote_threshold_percentage: Option<u8>,

        #[arg(long)]
        min_council_weight_to_create_proposal: Option<u64>,

        #[arg(long)]
        min_transaction_hold_up_time: Option<u32>,

        /// Max voting time in seconds
        #[arg(long)]
        max_voting_time: Option<u32>,

        #[arg(long)]
        proposal_cool_off_time: Option<u32>,

        #[arg(long)]
        min_comunity_weight_to_create_proposal: Option<u64>,
    },
    /// Get a governance configuration
    GetGovConfig,
}


