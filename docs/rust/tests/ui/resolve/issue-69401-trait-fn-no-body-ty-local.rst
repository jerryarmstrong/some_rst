tests/ui/resolve/issue-69401-trait-fn-no-body-ty-local.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {}

trait Foo {
    fn fn_with_type_named_same_as_local_in_param(b: b);
    //~^ ERROR cannot find type `b` in this scope [E0412]
}


