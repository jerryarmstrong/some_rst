tests/ui/extoption_env-not-defined.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    assert!(option_env!("__HOPEFULLY_DOESNT_EXIST__").is_none());
}


