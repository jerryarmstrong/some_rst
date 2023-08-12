programs/compute-budget/src/lib.rs
==================================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    use solana_program_runtime::declare_process_instruction;

pub const DEFAULT_COMPUTE_UNITS: u64 = 150;

declare_process_instruction!(
    process_instruction,
    DEFAULT_COMPUTE_UNITS,
    |_invoke_context| {
        // Do nothing, compute budget instructions handled by the runtime
        Ok(())
    }
);


