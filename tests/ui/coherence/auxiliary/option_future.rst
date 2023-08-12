tests/ui/coherence/auxiliary/option_future.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]
#![feature(negative_impls)]
#![feature(rustc_attrs)]
#![feature(with_negative_coherence)]

pub trait Future {}

impl<E> !Future for Option<E> where E: Sized {}


