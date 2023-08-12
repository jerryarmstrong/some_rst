src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0014_use_tree.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use *;
use ::*;
use ::{};
use {};
use foo::*;
use foo::{};
use ::foo::{a, b, c};


