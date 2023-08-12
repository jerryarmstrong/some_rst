saf/src/plan.rs
===============

Last edited: 2022-11-28 20:53:26

Contents:

.. code-block:: rs

    use crate::account_constraints::AccountConstraints;
use crate::account_info::AccountInfoContext;
use solana_program::account_info::AccountInfo;
use solana_program::msg;
use solana_program::program_error::ProgramError;

use crate::{AccountsError, Constraints};

// TODO IMPL Iter
pub struct AccountPlan<'entry> {
    accounts: &'entry [AccountInfo<'entry>],
    required_accounts: usize,
    curr: usize,
    errors: Vec<ProgramError>,
    fast_fail: bool,
}

impl<'entry> AccountPlan<'entry> {
    /// Create a new AccountPlan
    pub fn new(
        accounts: &'entry [AccountInfo<'entry>],
        required_size: usize,
        fast_fail: bool,
    ) -> Result<Self, ProgramError> {
        if accounts.len() < required_size {
            return Err(AccountsError::OutOfAccounts.into());
        }
        Ok(AccountPlan {
            accounts,
            required_accounts: required_size,
            curr: 0,
            errors: vec![],
            fast_fail,
        })
    }

    /// Add a required account to the plan with the given constraints. This auto unwraps the account for convenience.
    pub fn required_account<'action>(
        &mut self,
        name: &'static str,
        constraints: Constraints<'action>,
    ) -> Result<AccountInfoContext<'entry, 'action>, ProgramError> {
        self.prepare_account(name, constraints)
            .and_then(|s| s.ok_or(AccountsError::RequiredAccountMissing.into()))
    }

    /// Alias of [`prepare_account`](AccountPlan::prepare_account) for convenience.
    pub fn optional_account<'action>(
        &mut self,
        name: &'static str,
        constraints: Constraints<'action>,
    ) -> Result<Option<AccountInfoContext<'entry, 'action>>, ProgramError> {
        self.prepare_account(name, constraints)
    }

    /// Add an account to the plan with the given constraints. This method consumes one item in the accounts iterator and wraps it with the context.
    /// Before returning the constraints are validated.
    pub fn prepare_account<'action>(
        &mut self,
        name: &'static str,
        constraints: Constraints<'action>,
    ) -> Result<Option<AccountInfoContext<'entry, 'action>>, ProgramError> {
        let fail = self.curr <= self.required_accounts;
        let item = self.accounts.get(self.curr);
        self.curr += 1;
        if let Some(a) = item {
            let mut accx = AccountInfoContext {
                name,
                info: a.clone(), // TODO -> There is a way to avoid this
                bump: None,
                constraints,
            };
            let res: Result<(), ProgramError> = accx.validate_constraint().map_err(|e| e.into());
            return match (res, self.fast_fail) {
                (Err(e), true) => Err(e),
                (Err(e), false) => {
                    self.errors.push(e);
                    Ok(None)
                }
                _ => Ok(Some(accx)),
            };
        }
        if fail {
            Err(AccountsError::OutOfAccounts.into())
        } else {
            Ok(None)
        }
    }

    pub fn validate(&self) -> Result<(), ProgramError> {
        if self.fast_fail {
            Ok(())
        } else {
            if self.errors.is_empty() {
                Ok(())
            } else {
                let msg = self.errors.iter().fold(String::new(), |mut acc, e| {
                    acc.push_str(&e.to_string());
                    acc
                });
                msg!("Errors: {}", msg);
                Err(AccountsError::ValidationError(msg).into())
            }
        }
    }

    pub fn accounts_length(&self) -> usize {
        self.accounts.len()
    }
}

//TODO -> Macroize this
impl<'entry> AccountPlan<'entry> {
    /// Convenience method for adding a system program
    pub fn system_program<'action>(
        &mut self,
    ) -> Result<Option<AccountInfoContext<'entry, 'action>>, ProgramError> {
        self.prepare_account("system_program", Constraints::system_program())
    }

    /// Convenience method for adding a rent program
    pub fn rent<'action>(
        &mut self,
    ) -> Result<Option<AccountInfoContext<'entry, 'action>>, ProgramError> {
        self.prepare_account("rent", Constraints::rent())
    }

    /// Convenience method for adding lookup program
    pub fn address_lookup<'action>(
        &mut self,
    ) -> Result<Option<AccountInfoContext<'entry, 'action>>, ProgramError> {
        self.prepare_account("lookup", Constraints::address_lookup_program())
    }
}


