tests/ui/coherence/auxiliary/error_lib.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]
#![feature(negative_impls)]
#![feature(with_negative_coherence)]

pub trait Error {}
impl !Error for &str {}


