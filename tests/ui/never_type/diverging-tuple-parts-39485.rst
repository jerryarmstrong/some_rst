tests/ui/never_type/diverging-tuple-parts-39485.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // After #39485, this test used to pass, but that change was reverted
// due to numerous inference failures like #39808, so it now fails
// again. #39485 made it so that diverging types never propagate
// upward; but we now do propagate such types upward in many more
// cases.

fn g() {
    &panic!() //~ ERROR mismatched types
}

fn f() -> isize {
    (return 1, return 2) //~ ERROR mismatched types
}

fn main() {}


