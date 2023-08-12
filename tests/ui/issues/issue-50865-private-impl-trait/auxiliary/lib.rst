tests/ui/issues/issue-50865-private-impl-trait/auxiliary/lib.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: default miropt
//[miropt]compile-flags: -Z mir-opt-level=3
// ~^ This flag is for #77668, it used to be ICE.

#![crate_type = "lib"]

pub fn bar<P>( // Error won't happen if "bar" is not generic
    _baz: P,
) {
    hide_foo()();
}

fn hide_foo() -> impl Fn() { // Error won't happen if "iterate" hasn't impl Trait or has generics
    foo
}

fn foo() { // Error won't happen if "foo" isn't used in "iterate" or has generics
}


