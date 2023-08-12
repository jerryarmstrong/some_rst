rpc-client/src/lib.rs
=====================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    #![allow(clippy::integer_arithmetic)]

pub mod http_sender;
pub mod mock_sender;
pub mod nonblocking;
pub mod rpc_client;
pub mod rpc_sender;
pub mod spinner;

pub mod mock_sender_for_cli {
    /// Magic `SIGNATURE` value used by `solana-cli` unit tests.
    /// Please don't use this constant.
    pub const SIGNATURE: &str =
        "43yNSFC6fYTuPgTNFFhF4axw7AfWxB2BPdurme8yrsWEYwm8299xh8n6TAHjGymiSub1XtyxTNyd9GBfY2hxoBw8";
}


