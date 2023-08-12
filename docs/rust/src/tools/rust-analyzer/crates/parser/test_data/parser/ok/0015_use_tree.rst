src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0015_use_tree.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use foo as bar;
use foo::{a as b, *, ::*, ::foo as x};


