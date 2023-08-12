src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0040_crate_keyword_vis.rs
==========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    crate fn main() { }
struct S { crate field: u32 }
struct T(crate u32);


