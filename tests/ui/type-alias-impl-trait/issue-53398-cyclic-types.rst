tests/ui/type-alias-impl-trait/issue-53398-cyclic-types.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

type Foo = impl Fn() -> Foo;

fn foo() -> Foo {
//~^ ERROR: overflow evaluating the requirement
    foo
}

fn main() {}


