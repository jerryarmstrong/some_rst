ws/src/lib.rs
=============

Last edited: 2018-12-07 22:58:36

Contents:

.. code-block:: rs

    //! `WebSockets` server.

#![warn(missing_docs)]

extern crate solana_jsonrpc_server_utils as server_utils;
extern crate parking_lot;
extern crate slab;

pub extern crate solana_ws as ws;
pub extern crate solana_jsonrpc_core as jsonrpc_core;

#[macro_use]
extern crate error_chain;
#[macro_use]
extern crate log;

mod error;
mod metadata;
mod server;
mod server_builder;
mod session;
#[cfg(test)]
mod tests;

use jsonrpc_core as core;

pub use self::error::{Error, ErrorKind, Result};
pub use self::metadata::{RequestContext, MetaExtractor, NoopExtractor, Sender};
pub use self::session::{RequestMiddleware, MiddlewareAction};
pub use self::server::{CloseHandle, Server};
pub use self::server_builder::ServerBuilder;
pub use self::server_utils::cors::Origin;
pub use self::server_utils::hosts::{Host, DomainsValidation};
pub use self::server_utils::tokio;
pub use self::server_utils::session::{SessionId, SessionStats};


