tests/ui/rmeta/rmeta-pass.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --emit=metadata
// aux-build:rmeta-meta.rs
// no-prefer-dynamic
// build-pass (FIXME(62277): could be check-pass?)

// Check that building a metadata crate works with a dependent, metadata-only
// crate.
// This is a cfail test since there is no executable to run.

extern crate rmeta_meta;
use rmeta_meta::Foo;

pub fn main() {
    let _ = Foo { field: 42 };
}


