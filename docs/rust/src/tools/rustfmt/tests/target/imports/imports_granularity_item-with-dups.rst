src/tools/rustfmt/tests/target/imports/imports_granularity_item-with-dups.rs
============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-imports_granularity: Item

use crate::lexer;
use crate::lexer::tokens::TokenData;
use crate::lexer::{self};


