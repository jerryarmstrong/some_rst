tests/ui/imports/local-modularized-tricky-pass-1.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)

macro_rules! define_exported { () => {
    #[macro_export]
    macro_rules! exported {
        () => ()
    }
}}

mod inner1 {
    use super::*;
    exported!();
}

mod inner2 {
    define_exported!();
}

fn main() {}


