src/tools/rustfmt/tests/target/issue-3241.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-edition: 2018

use ::baz::{bar, foo};
use ::ignore;
use ::ignore::some::more;
use ::*;
use ::{bar, foo};

fn main() {
    println!("Hello, world!");
}


