runtime/src/runtime_config.rs
=============================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    use solana_program_runtime::compute_budget::ComputeBudget;

/// Encapsulates flags that can be used to tweak the runtime behavior.
#[derive(AbiExample, Debug, Default, Clone)]
pub struct RuntimeConfig {
    pub compute_budget: Option<ComputeBudget>,
    pub log_messages_bytes_limit: Option<usize>,
    pub transaction_account_lock_limit: Option<usize>,
}


