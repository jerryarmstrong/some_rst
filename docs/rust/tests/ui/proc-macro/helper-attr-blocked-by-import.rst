tests/ui/proc-macro/helper-attr-blocked-by-import.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)
// aux-build:test-macros.rs

#[macro_use(Empty)]
extern crate test_macros;

use self::one::*;
use self::two::*;

mod empty_helper {}

mod one {
    use empty_helper;

    #[derive(Empty)]
    #[empty_helper]
    struct One;
}

mod two {
    use empty_helper;

    #[derive(Empty)]
    #[empty_helper]
    struct Two;
}

fn main() {}


