tests/ui/rmeta/rmeta-lib-pass.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --emit=metadata
// aux-build:rmeta-rlib.rs
// no-prefer-dynamic
// build-pass (FIXME(62277): could be check-pass?)

// Check that building a metadata crate works with a dependent, rlib crate.
// This is a cfail test since there is no executable to run.

extern crate rmeta_rlib;
use rmeta_rlib::Foo;

pub fn main() {
    let _ = Foo { field: 42 };
}


