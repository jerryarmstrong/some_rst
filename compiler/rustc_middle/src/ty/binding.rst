compiler/rustc_middle/src/ty/binding.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use rustc_hir::{BindingAnnotation, ByRef, Mutability};

#[derive(Clone, PartialEq, TyEncodable, TyDecodable, Debug, Copy, HashStable)]
pub enum BindingMode {
    BindByReference(Mutability),
    BindByValue(Mutability),
}

TrivialTypeTraversalAndLiftImpls! { BindingMode, }

impl BindingMode {
    pub fn convert(BindingAnnotation(by_ref, mutbl): BindingAnnotation) -> BindingMode {
        match by_ref {
            ByRef::No => BindingMode::BindByValue(mutbl),
            ByRef::Yes => BindingMode::BindByReference(mutbl),
        }
    }
}


