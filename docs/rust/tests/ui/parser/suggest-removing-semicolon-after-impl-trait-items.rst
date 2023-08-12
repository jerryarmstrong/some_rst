tests/ui/parser/suggest-removing-semicolon-after-impl-trait-items.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

trait Foo {
    fn bar() {}; //~ ERROR non-item in item list
}

fn main() {}


