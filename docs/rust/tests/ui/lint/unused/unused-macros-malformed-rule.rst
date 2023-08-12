tests/ui/lint/unused/unused-macros-malformed-rule.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unused_macros)]

macro_rules! foo { //~ ERROR: unused macro definition
    (v) => {};
    () => 0; //~ ERROR: macro rhs must be delimited
}

macro_rules! bar {
    (v) => {};
    () => 0; //~ ERROR: macro rhs must be delimited
}

fn main() {
    bar!(v);
}


