tests/ui/deprecation/issue-84637-deprecated-associated-function.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![deny(deprecated)]

fn main() {
    let _foo = str::trim_left("   aoeu"); //~ ERROR use of deprecated associated function `core::str::<impl str>::trim_left`: superseded by `trim_start` [deprecated]

    let _bar = "   aoeu".trim_left(); //~ ERROR use of deprecated associated function `core::str::<impl str>::trim_left`: superseded by `trim_start` [deprecated]
}


