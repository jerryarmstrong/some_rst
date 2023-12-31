shank-idl/src/idl_error_code.rs
===============================

Last edited: 2023-07-29 23:58:28

Contents:

.. code-block:: rs

    use serde::{Deserialize, Serialize};
use shank_macro_impl::error::ProgramError;

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
pub struct IdlErrorCode {
    pub code: u32,
    pub name: String,
    #[serde(skip_serializing_if = "Option::is_none", default)]
    pub msg: Option<String>,
}

impl From<ProgramError> for IdlErrorCode {
    fn from(program_error: ProgramError) -> Self {
        let ProgramError {
            name, desc, code, ..
        } = program_error;
        Self {
            code,
            name,
            msg: Some(desc),
        }
    }
}


