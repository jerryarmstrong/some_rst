tests/ui/parser/issue-101477-enum.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#[allow(dead_code)]
enum Demo {
    A = 1,
    B == 2 //~ ERROR unexpected `==`
    //~^ expected item, found `==`
}

fn main() {}


