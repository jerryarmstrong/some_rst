tests/ui/native-library-link-flags/suggest-libname-only-1.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail
// compile-flags: --crate-type rlib
// error-pattern: could not find native static library `libfoo.a`
// error-pattern: only provide the library name `foo`, not the full filename

#[link(name = "libfoo.a", kind = "static")]
extern { }

pub fn main() { }


