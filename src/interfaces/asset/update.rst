src/interfaces/asset/update.rs
==============================

Last edited: 2022-08-04 13:38:52

Contents:

.. code-block:: rs

    use std::cell::RefMut;
use std::collections::{BTreeMap};
use solana_program::account_info::AccountInfo;
use crate::api::{DigitalAssetProtocolError};
use crate::interfaces::ContextAction;
use crate::lifecycle::Lifecycle;
use crate::blob::Asset;
use crate::generated::schema::owned::{ActionData};


pub struct UpdateV1<'info> {
    pub id: AccountInfo<'info>,
    pub owner: AccountInfo<'info>,
    pub payer: AccountInfo<'info>,
    pub payload: String,
}

impl<'info> UpdateV1<'info> {
    pub fn new(accounts: &[AccountInfo<'info>], action: ActionData) -> Result<(Self, usize), DigitalAssetProtocolError> {
        if let ActionData::UpdateAssetV1 {
            msg
        } = action {
            let program = accounts[0].clone();
            let system = accounts[1].clone();
            let rent = accounts[2].clone();
            let id = accounts[3].clone();
            let owner = accounts[4].clone();
            let payer = accounts[5].clone();
            return Ok((UpdateV1 {
                id,
                owner,
                payer,
                payload: msg.unwrap_or("".to_string()),
            }, 6)
            );
        }
        Err(DigitalAssetProtocolError::ActionError("Invalid Action format, action must be UpdateAssetV1".to_string()))
    }
}

impl ContextAction for UpdateV1<'_> {
    fn lifecycle(&self) -> &Lifecycle {
        &Lifecycle::Update
    }

    fn run(&self) -> Result<(), DigitalAssetProtocolError> {
        let data = self.id.try_borrow_mut_data().map_err(|_| {
            DigitalAssetProtocolError::ActionError("Issue with Borrowing Data".to_string())
        })?;



        Ok(())
    }
}

