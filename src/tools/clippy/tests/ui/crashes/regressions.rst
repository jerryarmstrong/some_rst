src/tools/clippy/tests/ui/crashes/regressions.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(clippy::disallowed_names, clippy::uninlined_format_args)]

pub fn foo(bar: *const u8) {
    println!("{:#p}", bar);
}

// Regression test for https://github.com/rust-lang/rust-clippy/issues/4917
/// <foo
struct A;

fn main() {}


