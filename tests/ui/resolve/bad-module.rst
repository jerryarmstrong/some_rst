tests/ui/resolve/bad-module.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let foo = thing::len(Vec::new());
    //~^ ERROR failed to resolve: use of undeclared crate or module `thing`

    let foo = foo::bar::baz();
    //~^ ERROR failed to resolve: use of undeclared crate or module `foo`
}


