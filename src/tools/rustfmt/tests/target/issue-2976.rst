src/tools/rustfmt/tests/target/issue-2976.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn a(_ /*comment*/: u8 /* toto */) {}
fn b(/*comment*/ _: u8 /* tata */) {}
fn c(_: /*comment*/ u8) {}


