tests/ui/parser/assoc-const-underscore-semantic-fail.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Semantically, an associated constant cannot use `_` as a name.

fn main() {}

const _: () = {
    pub trait A {
        const _: () = (); //~ ERROR `const` items in this context need a name
    }
    impl A for () {
        const _: () = (); //~ ERROR `const` items in this context need a name
        //~^ ERROR const `_` is not a member of trait `A`
    }
    struct B;
    impl B {
        const _: () = (); //~ ERROR `const` items in this context need a name
    }
};


