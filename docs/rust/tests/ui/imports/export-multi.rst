tests/ui/imports/export-multi.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

use m::f;
use m::g;

mod m {
    pub fn f() { }
    pub fn g() { }
}

pub fn main() { f(); g(); m::f(); m::g(); }


