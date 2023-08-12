client/src/nonblocking/quic_client.rs
=====================================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    #[deprecated(
    since = "1.15.0",
    note = "Please use `solana_quic_client::nonblocking::quic_client::QuicClientConnection` instead."
)]
pub use solana_quic_client::nonblocking::quic_client::QuicClientConnection as QuicTpuConnection;
pub use solana_quic_client::nonblocking::quic_client::{
    QuicClient, QuicClientCertificate, QuicLazyInitializedEndpoint,
};


