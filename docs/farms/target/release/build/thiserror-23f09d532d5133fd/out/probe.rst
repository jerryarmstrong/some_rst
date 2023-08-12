target/release/build/thiserror-23f09d532d5133fd/out/probe.rs
============================================================

Last edited: 2022-12-05 19:44:34

Contents:

.. code-block:: rs

    
    #![feature(provide_any)]

    use std::any::{Demand, Provider};

    fn _f<'a, P: Provider>(p: &'a P, demand: &mut Demand<'a>) {
        p.provide(demand);
    }


