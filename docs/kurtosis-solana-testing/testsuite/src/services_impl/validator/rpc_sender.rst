testsuite/src/services_impl/validator/rpc_sender.rs
===================================================

Last edited: 2021-03-14 22:40:05

Contents:

.. code-block:: rs

    use anyhow::Result;

use super::rpc_request::RpcRequest;

/*
NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
This entire file is copied from https://github.com/solana-labs/solana/blob/master/client/src/rpc_request.rs
because solana-client provides Ledger support, which means it has a dependency
on the 'hidapi' kernel module. This module won't compile under Docker-for-Mac
due to https://github.com/docker/for-mac/issues/5295
Therefore, we reimplement parts of the Solana client here as a hackaround
NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
*/

pub trait RpcSender {
    fn send(&self, request: RpcRequest, params: serde_json::Value) -> Result<serde_json::Value>;
}

