src/tools/rustfmt/tests/target/imports/imports_granularity_item-with-dups-StdExternalCrate-no-reorder.rs
========================================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-imports_granularity: Item
// rustfmt-reorder_imports: false
// rustfmt-group_imports: StdExternalCrate

use crate::lexer;
use crate::lexer::tokens::TokenData;
use crate::lexer::{self};


