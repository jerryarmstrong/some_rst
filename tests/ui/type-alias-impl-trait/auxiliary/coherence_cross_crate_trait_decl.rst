tests/ui/type-alias-impl-trait/auxiliary/coherence_cross_crate_trait_decl.rs
============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait SomeTrait {}

impl SomeTrait for () {}

// Adding this `impl` would cause errors in this crate's dependent,
// so it would be a breaking change. We explicitly don't add this impl,
// as the dependent crate already assumes this impl exists and thus already
// does not compile.
//impl SomeTrait for i32 {}


