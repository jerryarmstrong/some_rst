tests/ui/feature-gates/feature-gate-assoc-type-defaults.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // gate-test-associated_type_defaults

trait Foo {
    type Bar = u8; //~ ERROR associated type defaults are unstable
}

fn main() {}


