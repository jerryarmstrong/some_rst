tests/ui/dyn-star/check-size-at-cast-polymorphic-bad.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(dyn_star)]
#![allow(incomplete_features)]

use std::fmt::Debug;

fn dyn_debug(_: (dyn* Debug + '_)) {

}

fn polymorphic<T: Debug + ?Sized>(t: &T) {
    dyn_debug(t);
    //~^ ERROR `&T` needs to be a pointer-sized type
}

fn main() {}


