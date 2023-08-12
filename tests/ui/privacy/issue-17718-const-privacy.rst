tests/ui/privacy/issue-17718-const-privacy.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:issue-17718-const-privacy.rs

extern crate issue_17718_const_privacy as other;

use a::B; //~ ERROR: constant `B` is private
use other::{
    FOO,
    BAR, //~ ERROR: constant `BAR` is private
    FOO2,
};

mod a {
    const B: usize = 3;
}

fn main() {}


