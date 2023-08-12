ipc/src/lib.rs
==============

Last edited: 2018-12-07 22:58:36

Contents:

.. code-block:: rs

    //! Cross-platform JSON-RPC IPC transport.

#![warn(missing_docs)]

extern crate solana_jsonrpc_server_utils as server_utils;
extern crate parity_tokio_ipc;
extern crate tokio_service;
extern crate parking_lot;

pub extern crate solana_jsonrpc_core as jsonrpc_core;

#[macro_use] extern crate log;

#[cfg(test)] #[macro_use] extern crate lazy_static;
#[cfg(test)] extern crate env_logger;
#[cfg(test)] mod logger;

mod server;
mod select_with_weak;
mod meta;

use jsonrpc_core as jsonrpc;

pub use meta::{MetaExtractor, NoopExtractor, RequestContext};
pub use server::{Server, ServerBuilder, CloseHandle,SecurityAttributes};

pub use self::server_utils::{tokio, codecs::Separator};
pub use self::server_utils::session::{SessionStats, SessionId};


