tests/rustdoc-json/fn_pointer/generics.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-tidy-linelength

#![feature(no_core)]
#![no_core]

// @count "$.index[*][?(@.name=='WithHigherRankTraitBounds')].inner.type.inner.decl.inputs[*]" 1
// @is "$.index[*][?(@.name=='WithHigherRankTraitBounds')].inner.type.inner.decl.inputs[0][0]" '"val"'
// @is "$.index[*][?(@.name=='WithHigherRankTraitBounds')].inner.type.inner.decl.inputs[0][1].kind" '"borrowed_ref"'
// @is "$.index[*][?(@.name=='WithHigherRankTraitBounds')].inner.type.inner.decl.inputs[0][1].inner.lifetime" \"\'c\"
// @is "$.index[*][?(@.name=='WithHigherRankTraitBounds')].inner.type.inner.decl.output" '{ "kind": "primitive", "inner": "i32" }'
// @count "$.index[*][?(@.name=='WithHigherRankTraitBounds')].inner.type.inner.generic_params[*]" 1
// @is "$.index[*][?(@.name=='WithHigherRankTraitBounds')].inner.type.inner.generic_params[0].name" \"\'c\"
// @is "$.index[*][?(@.name=='WithHigherRankTraitBounds')].inner.type.inner.generic_params[0].kind" '{ "lifetime": { "outlives": [] } }'
pub type WithHigherRankTraitBounds = for<'c> fn(val: &'c i32) -> i32;


