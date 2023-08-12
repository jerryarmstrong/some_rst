tests/ui/resolve/bad-expr-path.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod m1 {}

fn main(arguments: Vec<String>) { //~ ERROR `main` function has wrong type
    log(debug, m1::arguments);
    //~^ ERROR cannot find function `log` in this scope
    //~| ERROR cannot find value `debug` in this scope
    //~| ERROR cannot find value `arguments` in module `m1`
}


