tests/ui/native-library-link-flags/link-arg-from-rs.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // link-arg is not supposed to be usable in #[link] attributes

// compile-flags:
// error-pattern: error[E0458]: unknown link kind `link-arg`, expected one of: static, dylib, framework, raw-dylib

#[link(kind = "link-arg")]
extern "C" {}
pub fn main() {}


