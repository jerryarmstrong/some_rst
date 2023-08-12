src/tools/clippy/tests/ui-toml/fn_params_excessive_bools/test.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::fn_params_excessive_bools)]

fn f(_: bool) {}
fn g(_: bool, _: bool) {}

fn main() {}


