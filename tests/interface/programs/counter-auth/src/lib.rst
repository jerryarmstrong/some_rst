tests/interface/programs/counter-auth/src/lib.rs
================================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: rs

    //! counter-auth is an example of a program *implementing* an external program
//! interface. Here the `counter::Auth` trait, where we only allow a count
//! to be incremented if it changes the counter from odd -> even or even -> odd.
//! Creative, I know. :P.

use anchor_lang::prelude::*;
use counter::Auth;

declare_id!("Aws2XRVHjNqCUbMmaU245ojT2DBJFYX58KVo2YySEeeP");

#[program]
pub mod counter_auth {
    use super::*;

    #[state]
    pub struct CounterAuth;

    impl<'info> Auth<'info, Empty> for CounterAuth {
        fn is_authorized(_ctx: Context<Empty>, current: u64, new: u64) -> Result<()> {
            if current % 2 == 0 {
                if new % 2 == 0 {
                    return Err(ProgramError::Custom(15000).into()); // Arbitrary error code.
                }
            } else {
                if new % 2 == 1 {
                    return Err(ProgramError::Custom(16000).into()); // Arbitrary error code.
                }
            }
            Ok(())
        }
    }
}

#[derive(Accounts)]
pub struct Empty {}


