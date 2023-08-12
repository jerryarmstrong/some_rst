tests/ui/typeck/issue-104513-ice.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S;
fn f() {
    let _: S<impl Oops> = S; //~ ERROR cannot find trait `Oops` in this scope
    //~^ ERROR `impl Trait` only allowed in function and inherent method return types
}
fn main() {}


