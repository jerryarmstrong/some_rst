tests/ui/typeck/auxiliary/tdticc_coherence_lib.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(auto_traits, core)]
#![crate_type = "rlib"]

pub auto trait DefaultedTrait { }

pub struct Something<T> { t: T }


