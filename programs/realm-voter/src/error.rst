programs/realm-voter/src/error.rs
=================================

Last edited: 2023-06-01 19:30:16

Contents:

.. code-block:: rs

    use anchor_lang::prelude::*;

#[error_code]
pub enum RealmVoterError {
    #[msg("Invalid Realm Authority")]
    InvalidRealmAuthority,

    #[msg("Invalid Realm for Registrar")]
    InvalidRealmForRegistrar,

    #[msg("Invalid VoterWeightRecord Realm")]
    InvalidVoterWeightRecordRealm,

    #[msg("Invalid VoterWeightRecord Mint")]
    InvalidVoterWeightRecordMint,

    #[msg("TokenOwnerRecord from own realm is not allowed")]
    TokenOwnerRecordFromOwnRealmNotAllowed,

    #[msg("Governance program not configured")]
    GovernanceProgramNotConfigured,

    #[msg("Governing TokenOwner must match")]
    GoverningTokenOwnerMustMatch,
}


