src/tools/rust-analyzer/crates/ide-assists/src/assist_config.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Settings for tweaking assists.
//!
//! The fun thing here is `SnippetCap` -- this type can only be created in this
//! module, and we use to statically check that we only produce snippet
//! assists if we are allowed to.

use ide_db::{imports::insert_use::InsertUseConfig, SnippetCap};

use crate::AssistKind;

#[derive(Clone, Debug, PartialEq, Eq)]
pub struct AssistConfig {
    pub snippet_cap: Option<SnippetCap>,
    pub allowed: Option<Vec<AssistKind>>,
    pub insert_use: InsertUseConfig,
    pub prefer_no_std: bool,
    pub assist_emit_must_use: bool,
}


