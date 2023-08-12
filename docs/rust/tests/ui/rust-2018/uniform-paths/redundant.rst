tests/ui/rust-2018/uniform-paths/redundant.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// edition:2018

use std;
use std::io;

mod foo {
    pub use std as my_std;
}

mod bar {
    pub use std::{self};
}

fn main() {
    let _ = io::stdout();
    let _ = self::std::io::stdout();
    let _ = foo::my_std::io::stdout();
    let _ = bar::std::io::stdout();
}


