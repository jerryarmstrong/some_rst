saf/src/account_constraints.rs
==============================

Last edited: 2022-11-28 20:53:26

Contents:

.. code-block:: rs

    use crate::account_info::AccountInfoContext;
use crate::utils::{assert_key_equal, derive};
use crate::AccountsError;

pub trait AccountConstraints {
    fn validate_constraint(&mut self) -> Result<(), AccountsError>;
}

impl<'entry, 'action> AccountConstraints for AccountInfoContext<'entry, 'action> {
    fn validate_constraint(&mut self) -> Result<(), AccountsError> {
        if self.constraints.program && !self.info.executable {
            return Err(AccountsError::ValidationError(format!(
                "Account with key {} needs to be a program",
                self.info.key
            )));
        }

        if !self.constraints.program && self.info.executable {
            return Err(AccountsError::ValidationError(format!(
                "Account with key {} can't be a program",
                self.info.key
            )));
        }

        if self.constraints.writable && !self.info.is_writable {
            return Err(AccountsError::ValidationError(format!(
                "Account with key {} needs to be writable",
                self.info.key
            )));
        }
        // May need to change this to support optional signers
        if self.constraints.signer && !self.info.is_signer {
            return Err(AccountsError::ValidationError(format!(
                "Account with key {} needs to be a signer",
                self.info.key
            )));
        }

        if let Some(ob) = self.constraints.owned_by {
            assert_key_equal(&ob, self.info.owner)?;
        }

        if self.constraints.empty && self.info.data_len() > 0 && self.info.lamports() > 0 {
            return Err(AccountsError::ValidationError(format!(
                "Account with key {} can't be a signer",
                self.info.key
            )));
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
            (None, None) => Ok(()),
            _ => Err(AccountsError::ValidationError(format!(
                "Account with key {} has incorrect seeds",
                self.info.key
            ))),
        }?;
        Ok(())
    }
}


