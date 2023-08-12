src/tools/rustfmt/tests/target/issue-3118.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use {
    crate::foo::bar,
    bytes::{Buf, BufMut},
    std::io,
};

mod foo {
    pub mod bar {}
}

fn main() {}


