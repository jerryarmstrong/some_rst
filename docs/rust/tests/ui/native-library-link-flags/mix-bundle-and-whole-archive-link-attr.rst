tests/ui/native-library-link-flags/mix-bundle-and-whole-archive-link-attr.rs
============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zunstable-options --crate-type rlib
// build-fail
// error-pattern: the linking modifiers `+bundle` and `+whole-archive` are not compatible with each other when generating rlibs

#[link(name = "mylib", kind = "static", modifiers = "+bundle,+whole-archive")]
extern "C" { }

fn main() { }


