src/tools/clippy/tests/ui/enum_glob_use.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![warn(clippy::enum_glob_use)]
#![allow(unused)]
#![warn(unused_imports)]

use std::cmp::Ordering::*;

enum Enum {
    Foo,
}

use self::Enum::*;

mod in_fn_test {
    fn blarg() {
        use crate::Enum::*;

        let _ = Foo;
    }
}

mod blurg {
    pub use std::cmp::Ordering::*; // ok, re-export
}

fn main() {
    let _ = Foo;
    let _ = Less;
}


