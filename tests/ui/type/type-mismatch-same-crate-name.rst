tests/ui/type/type-mismatch-same-crate-name.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:crate_a1.rs
// aux-build:crate_a2.rs

// This tests the extra note reported when a type error deals with
// seemingly identical types.
// The main use case of this error is when there are two crates
// (generally different versions of the same crate) with the same name
// causing a type mismatch. Here, we simulate that error using block-scoped
// aliased `extern crate` declarations.

fn main() {
    let foo2 = {extern crate crate_a2 as a; a::Foo};
    let bar2 = {extern crate crate_a2 as a; a::bar()};
    {
        extern crate crate_a1 as a;
        a::try_foo(foo2);
        //~^ ERROR mismatched types
        //~| perhaps two different versions of crate `crate_a1`
        //~| expected struct `main::a::Foo`
        a::try_bar(bar2);
        //~^ ERROR mismatched types
        //~| perhaps two different versions of crate `crate_a1`
        //~| expected trait `main::a::Bar`
        //~| expected struct `Box<(dyn main::a::Bar + 'static)>`
        //~| found struct `Box<dyn main::a::Bar>`
    }
}


