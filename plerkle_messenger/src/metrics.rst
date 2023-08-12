plerkle_messenger/src/metrics.rs
================================

Last edited: 2023-08-03 21:06:53

Contents:

.. code-block:: rs

    #[macro_export]
macro_rules! metric {
    {$($block:stmt;)*} => {
            if cadence_macros::is_global_default_set() {
                $(
                    $block
                )*
            }
    };
}


