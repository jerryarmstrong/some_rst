tcp/src/lib.rs
==============

Last edited: 2018-12-07 22:58:36

Contents:

.. code-block:: rs

    //! jsonrpc server over tcp/ip
//!
//! ```no_run
//! extern crate solana_jsonrpc_core as jsonrpc_core;
//! extern crate solana_jsonrpc_tcp_server as jsonrpc_tcp_server;
//!
//! use jsonrpc_core::*;
//! use jsonrpc_tcp_server::ServerBuilder;
//!
//! fn main() {
//! 	let mut io = IoHandler::default();
//! 	io.add_method("say_hello", |_params| {
//! 		Ok(Value::String("hello".to_string()))
//! 	});
//! 	let server = ServerBuilder::new(io)
//!			.start(&"0.0.0.0:0".parse().unwrap())
//!			.expect("Server must start with no issues.");
//!
//!		server.wait();
//! }
//! ```

#![warn(missing_docs)]

extern crate solana_jsonrpc_server_utils as server_utils;
extern crate parking_lot;
extern crate tokio_service;

pub extern crate solana_jsonrpc_core as jsonrpc_core;

#[macro_use] extern crate log;

#[cfg(test)] #[macro_use] extern crate lazy_static;
#[cfg(test)] extern crate env_logger;

mod dispatch;
mod meta;
mod server;
mod service;

#[cfg(test)] mod logger;
#[cfg(test)] mod tests;

use jsonrpc_core as jsonrpc;

pub use dispatch::{Dispatcher, PushMessageError};
pub use meta::{MetaExtractor, RequestContext};
pub use server::{ServerBuilder, Server};
pub use self::server_utils::{tokio, codecs::Separator};


