tests/ui/traits/alias/impl.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(trait_alias)]

trait DefaultAlias = Default;

impl DefaultAlias for () {} //~ ERROR expected trait, found trait alias

fn main() {}


