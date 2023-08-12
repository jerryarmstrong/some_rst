tests/rustdoc-json/unions/impl.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![no_std]

// @is "$.index[*][?(@.name=='Ux')].visibility" \"public\"
// @is "$.index[*][?(@.name=='Ux')].kind" \"union\"
pub union Ux {
    a: u32,
    b: u64
}

// @is "$.index[*][?(@.name=='Num')].visibility" \"public\"
// @is "$.index[*][?(@.name=='Num')].kind" \"trait\"
pub trait Num {}

// @count "$.index[*][?(@.name=='Ux')].inner.impls" 1
impl Num for Ux {}


