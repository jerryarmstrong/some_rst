tests/rustdoc/const-generics/type-alias.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

// @has foo/type.CellIndex.html '//div[@class="item-decl"]/pre[@class="rust"]' 'type CellIndex<const D: usize> = [i64; D];'
pub type CellIndex<const D: usize> = [i64; D];


