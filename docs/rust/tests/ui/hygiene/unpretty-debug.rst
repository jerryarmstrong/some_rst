tests/ui/hygiene/unpretty-debug.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: -Zunpretty=expanded,hygiene

// Don't break whenever Symbol numbering changes
// normalize-stdout-test "\d+#" -> "0#"

// minimal junk
#![feature(no_core)]
#![no_core]

macro_rules! foo {
    ($x: ident) => { y + $x }
}

fn bar() {
    let x = 1;
    foo!(x)
}

fn y() {}


