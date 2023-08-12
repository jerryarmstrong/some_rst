tests/ui/pub/pub-restricted-non-path.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(pub_restricted)]

pub (.) fn afn() {} //~ ERROR expected identifier

fn main() {}


