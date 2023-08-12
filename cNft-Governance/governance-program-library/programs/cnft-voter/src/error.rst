cNft-Governance/governance-program-library/programs/cnft-voter/src/error.rs
===========================================================================

Last edited: 2023-07-14 15:51:14

Contents:

.. code-block:: rs

    use anchor_lang::prelude::*;

#[error_code]
pub enum CompressedNftVoterError {
    #[msg("Invalid instruction")]
    InvalidInstruction,

    #[msg("Collection not found")]
    CollectionNotFound,

    #[msg("Invalid Realm Authoritu")]
    InvalidRealmAuthority,

    #[msg("Invalid Token Owner For Voter Weight Record")]
    InvalidTokenOwnerForVoterWeightRecord,

    #[msg("Voter Doest Not Own NFT")]
    VoterDoesNotOwnNft,

    #[msg("Duplicated NFT Detected")]
    DuplicatedNftDetected,

    #[msg("Invalid NFT Amount")]
    InvalidNftAmount,

    #[msg("Invalid Account Owner")]
    InvalidAccountOwner,

    #[msg("Token Metadata Does Not Match")]
    TokenMetadataDoesNotMatch,

    #[msg("Missing Metadata Collection")]
    MissingMetadataCollection,

    #[msg("Collection Must Be Verified")]
    CollectionMustBeVerified,

    #[msg("Invalid Voter Weight Record Realm")]
    InvalidVoterWeightRecordRealm,

    #[msg("Invalid Voter Weight Record Realm")]
    InvalidVoterWeightRecordMint,

    #[msg("Cast Vote Is Not Allowed")]
    CastVoteIsNotAllowed,

    #[msg("Invalid Vote Record Account")]
    InvalidVoteRecordAccount,

    #[msg("Vote Record Must Be Withdrawn")]
    VoteRecordMustBeWithdrawn,

    #[msg("Voter Weight Record Must Be Expired")]
    VoterWeightRecordMustBeExpired,

    #[msg("Invalid Proposal For NFT Vote Record")]
    InvalidProposalForNftVoteRecord,

    #[msg("Invalid Token Owner For NFT Vote Record")]
    InvalidTokenOwnerForNftVoteRecord,

    #[msg("Invalid Realm For Registrar")]
    InvalidRealmForRegistrar,

    #[msg("Invalid Max Voter Weight Record Realm")]
    InvalidMaxVoterWeightRecordRealm,

    #[msg("Invalid Max Voter Weight Record Mint")]
    InvalidMaxVoterWeightRecordMint,

    #[msg("Invalid Collection Size")]
    InvalidCollectionSize,

    #[msg("NFT Already Voted")]
    NftAlreadyVoted,

    #[msg("Leaf Owner Must Be Payer")]
    LeafOwnerMustBePayer,

    #[msg("Leaf Owner Must Be Token Owner")]
    LeafOwnerMustBeTokenOwner,

    #[msg("Invalid Metadata")]
    InvalidMetadata,

    #[msg("Invalid AssetId")]
    InvalidAssetId,

    #[msg("Invalid NFT Collection")]
    InvalidCollectionMint,

    #[msg("Governance Token Owner Or Delegate Must Sign")]
    GoverningTokenOwnerOrDelegateMustSign,

    #[msg("Leaf Owner Must Be Voter Authority")]
    LeafOwnerMustBeVoterAuthority,
}


