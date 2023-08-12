src/tools/rust-analyzer/crates/syntax/test_data/parser/validation/0040_illegal_crate_kw_location.rs
===================================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use ::crate;
use {crate, foo::{crate::foo::bar::baz}};
use hello::crate;
use hello::crate::there;


