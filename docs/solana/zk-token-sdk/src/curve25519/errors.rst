zk-token-sdk/src/curve25519/errors.rs
=====================================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    use thiserror::Error;

#[derive(Error, Clone, Debug, Eq, PartialEq)]
pub enum Curve25519Error {
    #[error("pod conversion failed")]
    PodConversion,
}


