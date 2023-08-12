tests/ui/resolve/typo-suggestion-mistyped-in-path.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Struct;
//~^ NOTE function or associated item `fob` not found for this struct

impl Struct {
    fn foo() { }
}

mod module {
    fn foo() { }

    struct Struct;

    impl Struct {
        fn foo() { }
    }
}

trait Trait {
    fn foo();
}

fn main() {
    Struct::fob();
    //~^ ERROR no function or associated item named `fob` found for struct `Struct` in the current scope
    //~| NOTE function or associated item not found in `Struct`

    Struc::foo();
    //~^ ERROR failed to resolve: use of undeclared type `Struc`
    //~| NOTE use of undeclared type `Struc`

    modul::foo();
    //~^ ERROR failed to resolve: use of undeclared crate or module `modul`
    //~| NOTE use of undeclared crate or module `modul`

    module::Struc::foo();
    //~^ ERROR failed to resolve: could not find `Struc` in `module`
    //~| NOTE could not find `Struc` in `module`

    Trai::foo();
    //~^ ERROR failed to resolve: use of undeclared type `Trai`
    //~| NOTE use of undeclared type `Trai`
}


