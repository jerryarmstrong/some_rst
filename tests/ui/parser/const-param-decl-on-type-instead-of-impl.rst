tests/ui/parser/const-param-decl-on-type-instead-of-impl.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct NInts<const N: usize>([u8; N]);
impl NInts<const N: usize> {} //~ ERROR unexpected `const` parameter declaration

fn main() {
    let _: () = 42; //~ ERROR mismatched types
}

fn banana(a: <T<const N: usize>>::BAR) {}
//~^ ERROR unexpected `const` parameter declaration
//~| ERROR cannot find type `T` in this scope
fn chaenomeles() {
    path::path::Struct::<const N: usize>()
    //~^ ERROR unexpected `const` parameter declaration
    //~| ERROR failed to resolve: use of undeclared crate or module `path`
}


