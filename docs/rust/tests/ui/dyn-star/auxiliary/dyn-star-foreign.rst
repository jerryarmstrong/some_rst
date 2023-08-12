tests/ui/dyn-star/auxiliary/dyn-star-foreign.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(dyn_star)]
#![allow(incomplete_features)]

use std::fmt::Display;

pub fn require_dyn_star_display(_: dyn* Display) {}

fn works_locally() {
    require_dyn_star_display(1usize);
}


