tests/pretty/raw-str-nonexpr.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // needs-asm-support
// pp-exact

#[cfg(foo = r#"just parse this"#)]
extern crate blah as blah;

use std::arch::asm;

fn main() { unsafe { asm!(r###"blah"###); } }


