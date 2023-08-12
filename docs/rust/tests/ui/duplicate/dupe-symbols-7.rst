tests/ui/duplicate/dupe-symbols-7.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail

//
// error-pattern: entry symbol `main` declared multiple times

// FIXME https://github.com/rust-lang/rust/issues/59774
// normalize-stderr-test "thread.*panicked.*Metadata module not compiled.*\n" -> ""
// normalize-stderr-test "note:.*RUST_BACKTRACE=1.*\n" -> ""
#![allow(warnings)]

#[no_mangle]
fn main(){}


