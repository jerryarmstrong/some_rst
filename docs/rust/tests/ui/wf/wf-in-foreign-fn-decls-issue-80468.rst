tests/ui/wf/wf-in-foreign-fn-decls-issue-80468.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #80468.

#![crate_type = "lib"]

pub trait Trait {}

#[repr(transparent)]
pub struct Wrapper<T: Trait>(T);

#[repr(transparent)]
pub struct Ref<'a>(&'a u8);

impl Trait for Ref {} //~ ERROR:  implicit elided lifetime not allowed here

extern "C" {
    pub fn repro(_: Wrapper<Ref>); //~ ERROR: incompatible lifetime on type
}


