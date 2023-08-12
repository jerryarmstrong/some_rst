tests/ui/span/visibility-ty-params.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! m {
    ($p: path) => (pub(in $p) struct Z;)
}

struct S<T>(T);
m!{ S<u8> } //~ ERROR unexpected generic arguments in path
            //~| ERROR expected module, found struct `S`

mod m {
    m!{ m<> } //~ ERROR unexpected generic arguments in path
}

fn main() {}


