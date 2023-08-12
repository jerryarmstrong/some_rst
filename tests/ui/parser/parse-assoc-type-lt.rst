tests/ui/parser/parse-assoc-type-lt.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

trait Foo {
    type T;
    fn foo() -> Box<<Self as Foo>::T>;
}

fn main() {}


