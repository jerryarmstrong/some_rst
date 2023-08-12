tests/ui/typeck/issue-69378-ice-on-invalid-type-node-after-recovery.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #69378: no type for node after struct parse recovery

struct Foo { 0: u8 } //~ ERROR expected identifier

fn test(f: Foo) {
    Foo{foo: 4, ..f};
}

fn main() {}


