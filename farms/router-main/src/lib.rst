farms/router-main/src/lib.rs
============================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: rs

    #![forbid(unsafe_code)]

pub mod add_farm;
pub mod add_pool;
pub mod add_token;
pub mod add_vault;
mod entrypoint;
pub mod processor;
mod refdb_init;
pub mod refdb_instruction;
pub mod remove_farm;
pub mod remove_pool;
pub mod remove_token;
pub mod remove_vault;


