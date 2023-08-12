tests/ui/issues/issue-50865-private-impl-trait/main.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:lib.rs

// Regression test for #50865.
// When using generics or specifying the type directly, this example
// codegens `foo` internally. However, when using a private `impl Trait`
// function which references another private item, `foo` (in this case)
// wouldn't be codegenned until main.rs used `bar`, as with impl Trait
// it is not cast to `fn()` automatically to satisfy e.g.
// `fn foo() -> fn() { ... }`.

extern crate lib;

fn main() {
    lib::bar(()); // Error won't happen if bar is called from same crate
}


