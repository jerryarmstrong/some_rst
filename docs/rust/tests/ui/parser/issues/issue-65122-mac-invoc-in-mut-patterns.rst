tests/ui/parser/issues/issue-65122-mac-invoc-in-mut-patterns.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test; used to ICE with 'visit_mac_call disabled by default' due to a
// `MutVisitor` in `fn make_all_value_bindings_mutable` (`parse/parser/pat.rs`).

macro_rules! mac1 {
    ($eval:expr) => {
        let mut $eval = ();
        //~^ ERROR `mut` must be followed by a named binding
    };
}

macro_rules! mac2 {
    ($eval:pat) => {
        let mut $eval = ();
        //~^ ERROR `mut` must be followed by a named binding
        //~| ERROR expected identifier, found `does_not_exist!()`
    };
}

fn foo() {
    mac1! { does_not_exist!() }
    //~^ ERROR cannot find macro `does_not_exist` in this scope
    mac2! { does_not_exist!() }
    //~^ ERROR cannot find macro `does_not_exist` in this scope
}

fn main() {}


