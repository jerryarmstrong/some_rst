tests/run-make/env-dep-info/macro_use.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_use]
extern crate macro_def;

access_env_vars!();

fn main() {}


