tests/ui/resolve/editions-crate-root-2015.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2015

mod inner {
    fn global_inner(_: ::nonexistant::Foo) {
        //~^ ERROR failed to resolve: maybe a missing crate `nonexistant`?
    }
    fn crate_inner(_: crate::nonexistant::Foo) {
        //~^ ERROR failed to resolve: maybe a missing crate `nonexistant`?
    }

    fn bare_global(_: ::nonexistant) {
        //~^ ERROR cannot find type `nonexistant` in the crate root
    }
    fn bare_crate(_: crate::nonexistant) {
        //~^ ERROR cannot find type `nonexistant` in the crate root
    }
}

fn main() {

}


