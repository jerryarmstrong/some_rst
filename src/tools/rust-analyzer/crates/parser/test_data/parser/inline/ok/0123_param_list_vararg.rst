src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0123_param_list_vararg.rs
==========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "C" { fn printf(format: *const i8, ..., _: u8) -> i32; }


