tests/ui/reachable/unreachable-variant.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:unreachable_variant.rs

extern crate unreachable_variant as other;

fn main() {
    let _x = other::super_sekrit::sooper_sekrit::baz; //~ ERROR is private
}


