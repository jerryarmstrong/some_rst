programs/wbtc/src/macros.rs
===========================

Last edited: 2023-06-16 20:26:13

Contents:

.. code-block:: rs

    #[macro_export]
macro_rules! gen_mint_seeds {
    ($config:expr) => {
        &[CONFIG_SEED_PREFIX.as_bytes(), &[$config.bump]]
    };
}


