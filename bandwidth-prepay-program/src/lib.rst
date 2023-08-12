bandwidth-prepay-program/src/lib.rs
===================================

Last edited: 2019-08-29 17:32:23

Contents:

.. code-block:: rs

    #[macro_export]
macro_rules! bandwidth_prepay_program {
    () => {
        (
            "bandwidth_prepay_program".to_string(),
            bandwidth_prepay_api::id(),
        )
    };
}

use bandwidth_prepay_api::bandwidth_prepay_processor::process_instruction;
solana_sdk::solana_entrypoint!(process_instruction);


