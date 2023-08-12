target/release/build/thiserror-57263f4b309f1fd0/out/probe.rs
============================================================

Last edited: 2022-12-05 19:44:34

Contents:

.. code-block:: rs

    
    #![feature(provide_any)]

    use std::any::{Demand, Provider};

    fn _f<'a, P: Provider>(p: &'a P, demand: &mut Demand<'a>) {
        p.provide(demand);
    }


