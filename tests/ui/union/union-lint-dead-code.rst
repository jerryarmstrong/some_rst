tests/ui/union/union-lint-dead-code.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: mirunsafeck thirunsafeck
// [thirunsafeck]compile-flags: -Z thir-unsafeck

#![deny(dead_code)]

union Foo {
    x: usize,
    b: bool, //~ ERROR: field `b` is never read
    _unused: u16,
}

fn field_read(f: Foo) -> usize {
    unsafe { f.x }
}

fn main() {
    let _ = field_read(Foo { x: 2 });
}


