tests/ui/resolve/editions-crate-root-2018.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

mod inner {
    fn global_inner(_: ::nonexistant::Foo) {
        //~^ ERROR failed to resolve: could not find `nonexistant` in the list of imported crates
    }
    fn crate_inner(_: crate::nonexistant::Foo) {
        //~^ ERROR failed to resolve: could not find `nonexistant` in the crate root
    }

    fn bare_global(_: ::nonexistant) {
        //~^ ERROR cannot find crate `nonexistant` in the list of imported crates
    }
    fn bare_crate(_: crate::nonexistant) {
        //~^ ERROR cannot find type `nonexistant` in the crate root
    }
}

fn main() {

}


