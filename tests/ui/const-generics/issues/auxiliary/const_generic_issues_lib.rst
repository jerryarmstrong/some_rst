tests/ui/const-generics/issues/auxiliary/const_generic_issues_lib.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generic_const_exprs)]
#![allow(incomplete_features)]

// All of these three items must be in `lib2` to reproduce the error

pub trait TypeFn {
    type Output;
}

pub struct GenericType<const B: i8>;

// Removing the braces around `42` resolves the crash
impl TypeFn for GenericType<{ 40 + 2 }> {
    type Output = ();
}


