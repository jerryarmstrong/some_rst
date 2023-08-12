src/api.rs
==========

Last edited: 2022-08-04 13:38:52

Contents:

.. code-block:: rs

    use std::cell::{Ref, RefMut};
use bebop::{DeserializeError, Record};
use solana_program::{
    decode_error::DecodeError,
    msg,
    program_error::{PrintProgramError, ProgramError},
};
use solana_program::account_info::AccountInfo;
use solana_program::pubkey::Pubkey;
use thiserror::Error;
use crate::api::DigitalAssetProtocolError::ActionError;
use crate::interfaces::{asset};
use crate::validation::{assert_key_equal, cmp_pubkeys};
use crate::generated::schema::owned::{
    Action as IxAction,
    Interface,
    ActionData,
};
use crate::interfaces::ContextAction;

pub struct Action<'info> {
    pub standard: Interface,
    pub program_id: Pubkey,
    pub context: Box<dyn ContextAction + 'info>,
    pub remaining_accounts: Vec<AccountInfo<'info>>,
}

impl<'info> Action<'info> {
    pub fn run(&mut self) -> Result<(), DigitalAssetProtocolError> {
        self.context.run()
    }

    fn match_context(accounts: &[AccountInfo<'info>], action_data: ActionData) -> Result<(Box<dyn ContextAction + 'info>, usize), DigitalAssetProtocolError> {
        match action_data {
            ActionData::CreateAssetV1 { .. } => {
                let d = asset::CreateV1::new(accounts, action_data)?;
                Ok((Box::new(d.0), d.1))
            }
            ActionData::UpdateAssetV1 { .. } => {
                let d = asset::UpdateV1::new(accounts, action_data)?;
                Ok((Box::new(d.0), d.1))
            }
            _ => Err(DigitalAssetProtocolError::InterfaceNoImpl)
        }
    }

    pub fn from_instruction(program_id: &Pubkey,
                            accounts: &'info [AccountInfo<'info>],
                            instruction_data: &'info [u8]) -> Result<Action<'info>, DigitalAssetProtocolError> {
        let action = IxAction::deserialize(instruction_data)
            .map_err(|res| {
                DigitalAssetProtocolError::DeError(res.to_string())
            })?;

        return match action.standard {
            Interface::Nft => {
                let action_context = Action::match_context(accounts, action.data)?;
                Ok(Action {
                    standard: action.standard,
                    program_id: program_id.clone(),
                    context: action_context.0,
                    remaining_accounts: accounts[action_context.1..].to_vec(),
                })
            }
            _ => Err(DigitalAssetProtocolError::InterfaceNoImpl)
        };
    }
}


#[derive(Error, Debug)]
pub enum DigitalAssetProtocolError {
    #[error("Error in Module: {0}")]
    ModuleError(String),

    #[error("Error in Interface: {0}")]
    InterfaceError(String),

    #[error("Error in EntryPoint: {0}")]
    EntryPointError(String),

    #[error("Error in Action Parsing: {0}")]
    ActionError(String),

    #[error("Deserialization failed: {0}")]
    DeError(String),

    #[error("Interface has no implementation")]
    InterfaceNoImpl,

}

impl PrintProgramError for DigitalAssetProtocolError {
    fn print<E>(&self) {
        msg!(&self.to_string());
    }
}

impl From<DigitalAssetProtocolError> for ProgramError {
    fn from(e: DigitalAssetProtocolError) -> Self {
        msg!(&e.to_string());
        ProgramError::Custom(0)
    }
}

impl Into<DigitalAssetProtocolError> for DeserializeError {
    fn into(self) -> DigitalAssetProtocolError {
        DigitalAssetProtocolError::DeError(self.to_string())
    }
}

impl<T> DecodeError<T> for DigitalAssetProtocolError {
    fn type_of() -> &'static str {
        "Dasset Error"
    }
}


pub fn derive(seeds: &[&[u8]], program_id: &Pubkey) -> (Pubkey, u8) {
    Pubkey::find_program_address(seeds, program_id)
}

pub struct Constraints<'info> {
    seeds: Option<&'info [&'info [u8]]>,
    program_id: Option<Pubkey>,
    key_equals: Option<Pubkey>,
    writable: bool,
    signer: bool,
    program: bool,
    empty: bool,
}

pub struct AccountInfoContext<'info> {
    pub info: AccountInfo<'info>,
    mut_data_ref: Option<RefMut<'info, &'info mut [u8]>>,
    data_ref: Option<Ref<'info, &'info mut [u8]>>,
    pub seeds: Option<&'info [&'info [u8]]>,
    pub bump: Option<u8>,
    pub constraints: Constraints<'info>,
}

pub trait AccountConstraints {
    fn validate_constraint(&mut self) -> Result<(), DigitalAssetProtocolError>;
}

impl<'info> AccountConstraints for AccountInfoContext<'info> {
    fn validate_constraint(&mut self) -> Result<(), DigitalAssetProtocolError> {
        if self.constraints.program && !self.info.executable {
            return Err(DigitalAssetProtocolError::InterfaceError(format!("Account with key {} needs to be a program", self.info.key)));
        }
        if self.constraints.writable && !self.info.is_writable {
            return Err(DigitalAssetProtocolError::InterfaceError(format!("Account with key {} needs to be writable", self.info.key)));
        }
        if self.constraints.signer && !self.info.is_signer {
            return Err(DigitalAssetProtocolError::InterfaceError(format!("Account with key {} needs to be a signer", self.info.key)));
        }
        if let Some(kef) = self.constraints.key_equals {
            assert_key_equal(&kef, self.info.key)?;
        }
        match (self.constraints.seeds, self.constraints.program_id) {
            (Some(seeds), Some(prg)) => {
                let (pubkey, bump) = derive(seeds, &prg);
                assert_key_equal(&pubkey, self.info.key)?;
                self.bump = Some(bump);
                Ok(())
            }
            _ => Err(DigitalAssetProtocolError::InterfaceError(format!("Account with key {} has incorrect seeds", self.info.key)))
        }?;
        Ok(())
    }
}


