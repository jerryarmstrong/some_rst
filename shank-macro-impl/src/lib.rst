shank-macro-impl/src/lib.rs
===========================

Last edited: 2023-07-29 23:58:28

Contents:

.. code-block:: rs

    pub mod account;
pub mod builder;
pub mod converters;
pub mod custom_type;
pub mod error;
pub mod instruction;
pub mod krate;
pub mod macros;
pub mod parsed_enum;
pub mod parsed_macro;
pub mod parsed_struct;
pub mod parsers;
pub mod types;

pub const DERIVE_ACCOUNT_ATTR: &str = "ShankAccount";
pub const DERIVE_CONTEXT_ATTR: &str = "ShankContext";
pub const DERIVE_BUILDER_ATTR: &str = "ShankBuilder";
pub const DERIVE_INSTRUCTION_ATTR: &str = "ShankInstruction";

pub mod syn {
    pub use syn::*;
}


