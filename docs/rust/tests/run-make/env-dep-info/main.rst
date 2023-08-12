tests/run-make/env-dep-info/main.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    env!("EXISTING_ENV");
    option_env!("EXISTING_OPT_ENV");
    option_env!("NONEXISTENT_OPT_ENV");
    option_env!("ESCAPE\nESCAPE\\");
}


