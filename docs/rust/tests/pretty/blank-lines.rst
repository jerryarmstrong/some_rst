tests/pretty/blank-lines.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --crate-type=lib

// pp-exact
fn f() -> [isize; 3] {
    let picard = 0;

    let data = 1;

    let worf = 2;


    let enterprise = [picard, data, worf];



    return enterprise;
}


