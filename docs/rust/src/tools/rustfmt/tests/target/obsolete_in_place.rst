src/tools/rustfmt/tests/target/obsolete_in_place.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // #2953

macro_rules! demo {
    ($a:ident <- $b:expr) => {};
}

fn main() {
    demo!(i <- 0);
}


