common/datatest-stable/src/lib.rs
=================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    //! `datatest-stable` is a very simple test harness intended to meet some of the needs provided by
//! the `datatest` crate when using a stable rust compiler without using the `RUSTC_BOOTSTRAP` hack
//! to use nightly features on the stable track.
//!
//! In order to setup data-driven tests for a particular test target you must do the following:
//! 1. Configure the test target by setting the following in the `Cargo.toml`
//! ```lang=toml
//! [[test]]
//! name = "<test target name>"
//! harness = false
//! ```
//!
//! 2. Call the `solana_libra_datatest_stable::harness!(testfn, root, pattern)` macro with the following
//! parameters:
//! * `testfn` - The test function to be executed on each matching input. This function must have
//!   the type `fn(&Path) -> solana_libra_datatest_stable::Result<()>`
//! * `root` - The path to the root directory where the input files live. This path is relative to
//!   the root of the crate.
//! * `pattern` - the regex used to match against and select each file to be tested.
//!
//! The three parameters can be repeated if you have multiple sets of data-driven tests to be run:
//! `solana_libra_datatest_stable::harness!(testfn1, root1, pattern1, testfn2, root2, pattern2)`

mod macros;
mod runner;
mod utils;

pub type Result<T> = ::std::result::Result<T, Box<dyn ::std::error::Error>>;

pub use self::runner::{runner, Requirements};


