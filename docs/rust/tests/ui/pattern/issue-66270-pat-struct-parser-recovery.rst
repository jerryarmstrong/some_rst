tests/ui/pattern/issue-66270-pat-struct-parser-recovery.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #66270, fixed by #66246

struct Bug {
    incorrect_field: 0,
    //~^ ERROR expected type
}

struct Empty {}

fn main() {
    let Bug {
        any_field: Empty {},
    } = Bug {};
}


