src/tools/rustfmt/tests/source/issue-3241.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-edition: 2018

use ::ignore;
use ::ignore::some::more;
use ::{foo, bar};
use ::*;
use ::baz::{foo, bar};

fn main() {
    println!("Hello, world!");
}


