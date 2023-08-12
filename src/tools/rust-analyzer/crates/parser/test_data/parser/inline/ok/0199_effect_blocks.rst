src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0199_effect_blocks.rs
======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f() { unsafe { } }
fn f() { const { } }
fn f() { async { } }
fn f() { async move { } }


