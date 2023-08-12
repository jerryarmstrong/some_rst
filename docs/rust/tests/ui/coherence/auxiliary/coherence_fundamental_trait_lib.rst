tests/ui/coherence/auxiliary/coherence_fundamental_trait_lib.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]
#![feature(fundamental)]

pub trait Misc {}

#[fundamental]
pub trait Fundamental<T> {}


