tests/ui/native-library-link-flags/suggest-libname-only-2.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail
// compile-flags: --crate-type rlib
// error-pattern: could not find native static library `bar.lib`
// error-pattern: only provide the library name `bar`, not the full filename

#[link(name = "bar.lib", kind = "static")]
extern { }

pub fn main() { }


