tests/ui/const-generics/auxiliary/generics_of_parent_impl_trait.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generic_const_exprs)]
#![allow(incomplete_features)]

// library portion of testing that `impl Trait<{ expr }>` doesnt
// ice because of a `DefKind::TyParam` parent
pub fn foo<const N: usize>(foo: impl Into<[(); N + 1]>) {
    foo.into();
}


