testsuite/src/execution_impl/solana_testsuite_args.rs
=====================================================

Last edited: 2021-03-14 22:40:05

Contents:

.. code-block:: rs

    use serde::{Deserialize, Serialize};

#[derive(Deserialize, Serialize)]
pub struct SolanaTestsuiteArgs {
    #[serde(rename = "normalImage")]
    pub normal_image: String,
}

