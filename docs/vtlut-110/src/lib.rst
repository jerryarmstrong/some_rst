src/lib.rs
==========

Last edited: 2022-10-31 20:56:14

Contents:

.. code-block:: rs

    pub(crate) use {
    serde::{Deserialize, Serialize},
    serde_json::json,
    solana_client::{
        nonblocking::rpc_client::RpcClient as AsyncRpcClient, rpc_client::RpcClient,
        rpc_config::RpcSendTransactionConfig, rpc_request::RpcRequest,
    },
    solana_program::{
        hash::Hash,
        instruction::CompiledInstruction,
        instruction::{Instruction, InstructionError},
        message::{
            v0::{LoadedAddresses, Message, MessageAddressTableLookup},
            AccountKeys, MessageHeader, VersionedMessage,
        },
        pubkey::Pubkey,
        slot_history::Slot,
    },
    solana_sdk::{
        commitment_config::{CommitmentConfig, CommitmentLevel},
        signature::{Keypair, Signature},
        transaction::VersionedTransaction,
    },
    solana_transaction_status::UiTransactionEncoding,
    std::{
        borrow::Cow,
        collections::BTreeMap,
        {ops::Deref, str::FromStr},
    },
    thiserror::Error,
};

pub mod constants;
pub mod errors;
pub mod instructions;
pub mod vt;

use crate::constants::*;

/// Program account states
#[derive(Debug, Serialize, Deserialize, PartialEq, Eq, Clone)]
#[allow(clippy::large_enum_variant)]
enum ProgramState {
    /// Account is not initialized.
    Uninitialized,
    /// Initialized `LookupTable` account.
    LookupTable(LookupTableMeta),
}

#[derive(Debug, PartialEq, Eq, Clone)]
pub struct AddressLookupTable<'a> {
    pub meta: LookupTableMeta,
    pub addresses: Cow<'a, [Pubkey]>,
}

impl<'a> AddressLookupTable<'a> {
    /// Efficiently deserialize an address table without allocating
    /// for stored addresses.
    pub fn deserialize(data: &'a [u8]) -> Result<AddressLookupTable<'a>, InstructionError> {
        let program_state: ProgramState =
            bincode::deserialize(data).map_err(|_| InstructionError::InvalidAccountData)?;

        let meta = match program_state {
            ProgramState::LookupTable(meta) => Ok(meta),
            ProgramState::Uninitialized => Err(InstructionError::UninitializedAccount),
        }?;

        let raw_addresses_data = data.get(LOOKUP_TABLE_META_SIZE..).ok_or({
            // Should be impossible because table accounts must
            // always be LOOKUP_TABLE_META_SIZE in length
            InstructionError::InvalidAccountData
        })?;
        let addresses: &[Pubkey] = bytemuck::try_cast_slice(raw_addresses_data).map_err(|_| {
            // Should be impossible because raw address data
            // should be aligned and sized in multiples of 32 bytes
            InstructionError::InvalidAccountData
        })?;

        Ok(Self {
            meta,
            addresses: Cow::Borrowed(addresses),
        })
    }
}

#[derive(Debug, Serialize, Deserialize, PartialEq, Eq, Clone)]
pub struct LookupTableMeta {
    /// Lookup tables cannot be closed until the deactivation slot is
    /// no longer "recent" (not accessible in the `SlotHashes` sysvar).
    pub deactivation_slot: Slot,
    /// The slot that the table was last extended. Address tables may
    /// only be used to lookup addresses that were extended before
    /// the current bank's slot.
    pub last_extended_slot: Slot,
    /// The start index where the table was last extended from during
    /// the `last_extended_slot`.
    pub last_extended_slot_start_index: u8,
    /// Authority address which must sign for each modification.
    pub authority: Option<Pubkey>,
    // Padding to keep addresses 8-byte aligned
    pub _padding: u16,
    // Raw list of addresses follows this serialized structure in
    // the account's data, starting from `LOOKUP_TABLE_META_SIZE`.
}

pub struct AddressLookupTableAccount {
    pub key: Pubkey,
    pub addresses: Vec<Pubkey>,
}

#[derive(PartialEq, Debug, Error, Eq, Clone)]
pub enum CompileError {
    #[error("account index overflowed during compilation")]
    AccountIndexOverflow,
    #[error("address lookup table index overflowed during compilation")]
    AddressTableLookupIndexOverflow,
    #[error("encountered unknown account key `{0}` during instruction compilation")]
    UnknownInstructionKey(Pubkey),
}

/// A helper struct to collect pubkeys compiled for a set of instructions
#[derive(Default, Debug, Clone, PartialEq, Eq)]
pub(crate) struct CompiledKeys {
    payer: Option<Pubkey>,
    key_meta_map: BTreeMap<Pubkey, CompiledKeyMeta>,
}

#[derive(Default, Debug, Clone, PartialEq, Eq)]
struct CompiledKeyMeta {
    is_signer: bool,
    is_writable: bool,
    is_invoked: bool,
}

impl CompiledKeys {
    /// Compiles the pubkeys referenced by a list of instructions and organizes by
    /// signer/non-signer and writable/readonly.
    pub(crate) fn compile(instructions: &[Instruction], payer: Option<Pubkey>) -> Self {
        let mut key_meta_map = BTreeMap::<Pubkey, CompiledKeyMeta>::new();
        for ix in instructions {
            let mut meta = key_meta_map.entry(ix.program_id).or_default();
            meta.is_invoked = true;
            for account_meta in &ix.accounts {
                let meta = key_meta_map.entry(account_meta.pubkey).or_default();
                meta.is_signer |= account_meta.is_signer;
                meta.is_writable |= account_meta.is_writable;
            }
        }
        if let Some(payer) = &payer {
            let mut meta = key_meta_map.entry(*payer).or_default();
            meta.is_signer = true;
            meta.is_writable = true;
        }
        Self {
            payer,
            key_meta_map,
        }
    }

    pub(crate) fn try_into_message_components(
        self,
    ) -> Result<(MessageHeader, Vec<Pubkey>), CompileError> {
        let try_into_u8 = |num: usize| -> Result<u8, CompileError> {
            u8::try_from(num).map_err(|_| CompileError::AccountIndexOverflow)
        };

        let Self {
            payer,
            mut key_meta_map,
        } = self;

        if let Some(payer) = &payer {
            key_meta_map.remove_entry(payer);
        }

        let writable_signer_keys: Vec<Pubkey> = payer
            .into_iter()
            .chain(
                key_meta_map
                    .iter()
                    .filter_map(|(key, meta)| (meta.is_signer && meta.is_writable).then_some(*key)),
            )
            .collect();
        let readonly_signer_keys: Vec<Pubkey> = key_meta_map
            .iter()
            .filter_map(|(key, meta)| (meta.is_signer && !meta.is_writable).then_some(*key))
            .collect();
        let writable_non_signer_keys: Vec<Pubkey> = key_meta_map
            .iter()
            .filter_map(|(key, meta)| (!meta.is_signer && meta.is_writable).then_some(*key))
            .collect();
        let readonly_non_signer_keys: Vec<Pubkey> = key_meta_map
            .iter()
            .filter_map(|(key, meta)| (!meta.is_signer && !meta.is_writable).then_some(*key))
            .collect();

        let signers_len = writable_signer_keys
            .len()
            .saturating_add(readonly_signer_keys.len());

        let header = MessageHeader {
            num_required_signatures: try_into_u8(signers_len)?,
            num_readonly_signed_accounts: try_into_u8(readonly_signer_keys.len())?,
            num_readonly_unsigned_accounts: try_into_u8(readonly_non_signer_keys.len())?,
        };

        let static_account_keys = std::iter::empty()
            .chain(writable_signer_keys)
            .chain(readonly_signer_keys)
            .chain(writable_non_signer_keys)
            .chain(readonly_non_signer_keys)
            .collect();

        Ok((header, static_account_keys))
    }

    pub(crate) fn try_extract_table_lookup(
        &mut self,
        lookup_table_account: &AddressLookupTableAccount,
    ) -> Result<Option<(MessageAddressTableLookup, LoadedAddresses)>, CompileError> {
        let (writable_indexes, drained_writable_keys) = self
            .try_drain_keys_found_in_lookup_table(&lookup_table_account.addresses, |meta| {
                !meta.is_signer && !meta.is_invoked && meta.is_writable
            })?;
        let (readonly_indexes, drained_readonly_keys) = self
            .try_drain_keys_found_in_lookup_table(&lookup_table_account.addresses, |meta| {
                !meta.is_signer && !meta.is_invoked && !meta.is_writable
            })?;

        // Don't extract lookup if no keys were found
        if writable_indexes.is_empty() && readonly_indexes.is_empty() {
            return Ok(None);
        }

        Ok(Some((
            MessageAddressTableLookup {
                account_key: lookup_table_account.key,
                writable_indexes,
                readonly_indexes,
            },
            LoadedAddresses {
                writable: drained_writable_keys,
                readonly: drained_readonly_keys,
            },
        )))
    }

    fn try_drain_keys_found_in_lookup_table(
        &mut self,
        lookup_table_addresses: &[Pubkey],
        key_meta_filter: impl Fn(&CompiledKeyMeta) -> bool,
    ) -> Result<(Vec<u8>, Vec<Pubkey>), CompileError> {
        let mut lookup_table_indexes = Vec::new();
        let mut drained_keys = Vec::new();

        for search_key in self
            .key_meta_map
            .iter()
            .filter_map(|(key, meta)| key_meta_filter(meta).then_some(key))
        {
            for (key_index, key) in lookup_table_addresses.iter().enumerate() {
                if key == search_key {
                    let lookup_table_index = u8::try_from(key_index)
                        .map_err(|_| CompileError::AddressTableLookupIndexOverflow)?;

                    lookup_table_indexes.push(lookup_table_index);
                    drained_keys.push(*search_key);
                    break;
                }
            }
        }

        for key in &drained_keys {
            self.key_meta_map.remove_entry(key);
        }

        Ok((lookup_table_indexes, drained_keys))
    }
}

pub trait TryCompileMsg {
    fn try_compile(
        payer: &Pubkey,
        instructions: &[Instruction],
        address_lookup_table_accounts: &[AddressLookupTableAccount],
        recent_blockhash: Hash,
    ) -> Result<Self, CompileError>
    where
        Self: Sized;
}

impl TryCompileMsg for Message {
    fn try_compile(
        payer: &Pubkey,
        instructions: &[Instruction],
        address_lookup_table_accounts: &[AddressLookupTableAccount],
        recent_blockhash: Hash,
    ) -> Result<Self, CompileError> {
        let mut compiled_keys = CompiledKeys::compile(instructions, Some(*payer));

        let mut address_table_lookups = Vec::with_capacity(address_lookup_table_accounts.len());
        let mut loaded_addresses_list = Vec::with_capacity(address_lookup_table_accounts.len());
        for lookup_table_account in address_lookup_table_accounts {
            if let Some((lookup, loaded_addresses)) =
                compiled_keys.try_extract_table_lookup(lookup_table_account)?
            {
                address_table_lookups.push(lookup);
                loaded_addresses_list.push(loaded_addresses);
            }
        }

        let (header, static_keys) = compiled_keys.try_into_message_components()?;
        let dynamic_keys = loaded_addresses_list.into_iter().collect();
        let account_keys = AccountKeys::new(&static_keys, Some(&dynamic_keys));
        let instructions = account_keys.try_compile_instructions(instructions)?;

        Ok(Self {
            header,
            account_keys: static_keys,
            recent_blockhash,
            instructions,
            address_table_lookups,
        })
    }
}

pub trait TryCompile {
    fn try_compile_instructions(
        &self,
        instructions: &[Instruction],
    ) -> Result<Vec<CompiledInstruction>, CompileError>;
}

impl TryCompile for AccountKeys<'_> {
    fn try_compile_instructions(
        &self,
        instructions: &[Instruction],
    ) -> Result<Vec<CompiledInstruction>, CompileError> {
        let mut account_index_map = BTreeMap::<&Pubkey, u8>::new();
        for (index, key) in self.iter().enumerate() {
            let index = u8::try_from(index).map_err(|_| CompileError::AccountIndexOverflow)?;
            account_index_map.insert(key, index);
        }

        let get_account_index = |key: &Pubkey| -> Result<u8, CompileError> {
            account_index_map
                .get(key)
                .cloned()
                .ok_or(CompileError::UnknownInstructionKey(*key))
        };

        instructions
            .iter()
            .map(|ix| {
                let accounts: Vec<u8> = ix
                    .accounts
                    .iter()
                    .map(|account_meta| get_account_index(&account_meta.pubkey))
                    .collect::<Result<Vec<u8>, CompileError>>()?;

                Ok(CompiledInstruction {
                    program_id_index: get_account_index(&ix.program_id)?,
                    data: ix.data.clone(),
                    accounts,
                })
            })
            .collect()
    }
}


