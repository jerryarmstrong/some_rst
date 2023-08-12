tests/ui/imports/extern-prelude-extern-crate-absolute-expanded.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)
// edition:2018

macro_rules! define_iso { () => {
    extern crate std as iso;
}}

::iso::thread_local! {
    static S: u8 = 0;
}

define_iso!();

fn main() {
    let s = S;
}


