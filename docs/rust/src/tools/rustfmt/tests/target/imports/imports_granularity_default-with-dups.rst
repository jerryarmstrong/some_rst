src/tools/rustfmt/tests/target/imports/imports_granularity_default-with-dups.rs
===============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::lexer;
use crate::lexer;
use crate::lexer::tokens::TokenData;
use crate::lexer::tokens::TokenData;
use crate::lexer::{self};
use crate::lexer::{self, tokens::TokenData};


