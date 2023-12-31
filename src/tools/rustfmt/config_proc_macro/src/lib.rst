src/tools/rustfmt/config_proc_macro/src/lib.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! This crate provides a derive macro for `ConfigType`.

#![recursion_limit = "256"]

mod attrs;
mod config_type;
mod item_enum;
mod item_struct;
mod utils;

use std::str::FromStr;

use proc_macro::TokenStream;
use syn::parse_macro_input;

#[proc_macro_attribute]
pub fn config_type(_args: TokenStream, input: TokenStream) -> TokenStream {
    let input = parse_macro_input!(input as syn::Item);
    let output = config_type::define_config_type(&input);

    #[cfg(feature = "debug-with-rustfmt")]
    {
        utils::debug_with_rustfmt(&output);
    }

    TokenStream::from(output)
}

/// Used to conditionally output the TokenStream for tests that need to be run on nightly only.
///
/// ```rust
/// # use rustfmt_config_proc_macro::nightly_only_test;
///
/// #[nightly_only_test]
/// #[test]
/// fn test_needs_nightly_rustfmt() {
///   assert!(true);
/// }
/// ```
#[proc_macro_attribute]
pub fn nightly_only_test(_args: TokenStream, input: TokenStream) -> TokenStream {
    // if CFG_RELEASE_CHANNEL is not set we default to nightly, hence why the default is true
    if option_env!("CFG_RELEASE_CHANNEL").map_or(true, |c| c == "nightly" || c == "dev") {
        input
    } else {
        // output an empty token stream if CFG_RELEASE_CHANNEL is not set to "nightly" or "dev"
        TokenStream::from_str("").unwrap()
    }
}

/// Used to conditionally output the TokenStream for tests that need to be run on stable only.
///
/// ```rust
/// # use rustfmt_config_proc_macro::stable_only_test;
///
/// #[stable_only_test]
/// #[test]
/// fn test_needs_stable_rustfmt() {
///   assert!(true);
/// }
/// ```
#[proc_macro_attribute]
pub fn stable_only_test(_args: TokenStream, input: TokenStream) -> TokenStream {
    // if CFG_RELEASE_CHANNEL is not set we default to nightly, hence why the default is false
    if option_env!("CFG_RELEASE_CHANNEL").map_or(false, |c| c == "stable") {
        input
    } else {
        // output an empty token stream if CFG_RELEASE_CHANNEL is not set or is not 'stable'
        TokenStream::from_str("").unwrap()
    }
}


