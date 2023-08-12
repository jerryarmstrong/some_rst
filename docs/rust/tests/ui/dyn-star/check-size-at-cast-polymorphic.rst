tests/ui/dyn-star/check-size-at-cast-polymorphic.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(dyn_star)]
#![allow(incomplete_features)]

use std::fmt::Debug;

fn dyn_debug(_: (dyn* Debug + '_)) {

}

fn polymorphic<T: Debug>(t: &T) {
    dyn_debug(t);
}

fn main() {}


