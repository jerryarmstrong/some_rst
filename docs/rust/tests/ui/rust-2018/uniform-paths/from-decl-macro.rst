tests/ui/rust-2018/uniform-paths/from-decl-macro.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)
// edition:2018

#![feature(decl_macro)]

macro check() {
    ::std::vec::Vec::<u8>::new()
}

fn main() {
    check!();
}


