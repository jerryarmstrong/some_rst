tests/codegen/dllimports/auxiliary/dummy.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // no-prefer-dynamic
#![crate_type = "staticlib"]

// Since codegen tests don't actually perform linking, this library doesn't need to export
// any symbols.  It's here just to satisfy the compiler looking for a .lib file when processing
// #[link(...)] attributes in wrapper.rs.


