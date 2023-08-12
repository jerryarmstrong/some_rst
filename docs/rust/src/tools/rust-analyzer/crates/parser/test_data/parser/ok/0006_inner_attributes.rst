src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0006_inner_attributes.rs
==================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![attr]
#![attr(true)]
#![attr(ident)]
#![attr(ident, 100, true, "true", ident = 100, ident = "hello", ident(100))]
#![attr(100)]
#![attr(enabled = true)]
#![enabled(true)]
#![attr("hello")]
#![repr(C, align = 4)]
#![repr(C, align(4))]

