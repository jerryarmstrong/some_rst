tests/ui/imports/import-trait-method.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    fn foo();
}

use Foo::foo; //~ ERROR not directly importable

fn main() { foo(); }


