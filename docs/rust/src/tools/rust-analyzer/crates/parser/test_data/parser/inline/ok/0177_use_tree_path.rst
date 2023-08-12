src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0177_use_tree_path.rs
======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use ::std;
use std::collections;

use self::m;
use super::m;
use crate::m;


