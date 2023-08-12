tests/ui/native-library-link-flags/mix-bundle-and-whole-archive.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Mixing +bundle and +whole-archive is not allowed

// compile-flags: -l static:+bundle,+whole-archive=mylib -Zunstable-options --crate-type rlib
// build-fail
// error-pattern: the linking modifiers `+bundle` and `+whole-archive` are not compatible with each other when generating rlibs

fn main() { }


