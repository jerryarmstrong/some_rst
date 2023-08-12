target/bpfel-unknown-unknown/release/build/thiserror-7fc945fa6579683e/out/probe.rs
==================================================================================

Last edited: 2022-12-05 19:44:34

Contents:

.. code-block:: rs

    
    #![feature(provide_any)]

    use std::any::{Demand, Provider};

    fn _f<'a, P: Provider>(p: &'a P, demand: &mut Demand<'a>) {
        p.provide(demand);
    }


