compiler/rustc_ty_utils/src/lib.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Various checks
//!
//! # Note
//!
//! This API is completely unstable and subject to change.

#![doc(html_root_url = "https://doc.rust-lang.org/nightly/nightly-rustc/")]
#![feature(let_chains)]
#![feature(never_type)]
#![feature(box_patterns)]
#![recursion_limit = "256"]

#[macro_use]
extern crate rustc_middle;
#[macro_use]
extern crate tracing;

use rustc_middle::ty::query::Providers;

mod abi;
mod assoc;
mod common_traits;
mod consts;
mod errors;
mod implied_bounds;
pub mod instance;
mod layout;
mod layout_sanity_check;
mod needs_drop;
pub mod representability;
mod structural_match;
mod ty;

pub fn provide(providers: &mut Providers) {
    abi::provide(providers);
    assoc::provide(providers);
    common_traits::provide(providers);
    consts::provide(providers);
    implied_bounds::provide(providers);
    layout::provide(providers);
    needs_drop::provide(providers);
    representability::provide(providers);
    ty::provide(providers);
    instance::provide(providers);
    structural_match::provide(providers);
}


