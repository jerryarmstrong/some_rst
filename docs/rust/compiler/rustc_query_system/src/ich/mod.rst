compiler/rustc_query_system/src/ich/mod.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! ICH - Incremental Compilation Hash

pub use self::hcx::StableHashingContext;
use rustc_span::symbol::{sym, Symbol};

mod hcx;
mod impls_hir;
mod impls_syntax;

pub const IGNORED_ATTRIBUTES: &[Symbol] = &[
    sym::cfg,
    sym::rustc_if_this_changed,
    sym::rustc_then_this_would_need,
    sym::rustc_dirty,
    sym::rustc_clean,
    sym::rustc_partition_reused,
    sym::rustc_partition_codegened,
    sym::rustc_expected_cgu_reuse,
];


