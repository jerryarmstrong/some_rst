tests/ui/tag-type-args.rs
=========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum Quux<T> { Bar }

fn foo(c: Quux) { assert!((false)); } //~ ERROR missing generics for enum `Quux`

fn main() { panic!(); }


