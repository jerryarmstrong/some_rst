src/tools/clippy/tests/ui/inline_fn_without_body.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![warn(clippy::inline_fn_without_body)]
#![allow(clippy::inline_always)]

trait Foo {
    #[inline]
    fn default_inline();

    #[inline(always)]
    fn always_inline();

    #[inline(never)]
    fn never_inline();

    #[inline]
    fn has_body() {}
}

fn main() {}


