macros/src/lib.rs
=================

Last edited: 2018-12-07 22:58:36

Contents:

.. code-block:: rs

    //! High level, typed wrapper for `jsonrpc_core`.
//!
//! Enables creation of "Service" objects grouping a set of RPC methods together in a typed manner.
//!
//! Example
//!
//! ```
//! extern crate solana_jsonrpc_core as jsonrpc_core;
//! #[macro_use] extern crate solana_jsonrpc_macros as jsonrpc_macros;
//! use jsonrpc_core::{IoHandler, Error, Result};
//! use jsonrpc_core::futures::future::{self, FutureResult};
//! build_rpc_trait! {
//! 	pub trait Rpc {
//! 		/// Returns a protocol version
//! 		#[rpc(name = "protocolVersion")]
//! 		fn protocol_version(&self) -> Result<String>;
//!
//! 		/// Adds two numbers and returns a result
//! 		#[rpc(name = "add")]
//! 		fn add(&self, u64, u64) -> Result<u64>;
//!
//! 		/// Performs asynchronous operation
//! 		#[rpc(name = "callAsync")]
//! 		fn call(&self, u64) -> FutureResult<String, Error>;
//! 	}
//! }
//! struct RpcImpl;
//! impl Rpc for RpcImpl {
//! 	fn protocol_version(&self) -> Result<String> {
//! 		Ok("version1".into())
//! 	}
//!
//! 	fn add(&self, a: u64, b: u64) -> Result<u64> {
//! 		Ok(a + b)
//! 	}
//!
//! 	fn call(&self, _: u64) -> FutureResult<String, Error> {
//! 		future::ok("OK".to_owned()).into()
//! 	}
//! }
//!
//! fn main() {
//!	  let mut io = IoHandler::new();
//!	  let rpc = RpcImpl;
//!
//!	  io.extend_with(rpc.to_delegate());
//! }
//! ```

#![warn(missing_docs)]

pub extern crate solana_jsonrpc_core as jsonrpc_core;
pub extern crate solana_jsonrpc_pubsub as jsonrpc_pubsub;
extern crate serde;

mod auto_args;
mod delegates;
mod util;

pub mod pubsub;

#[doc(hidden)]
pub use auto_args::{WrapAsync, WrapMeta, WrapSubscribe};

#[doc(hidden)]
pub use serde::{de::DeserializeOwned, Serialize};

pub use auto_args::Trailing;
pub use delegates::IoDelegate;
pub use util::to_value;


