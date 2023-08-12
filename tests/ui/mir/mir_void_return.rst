tests/ui/mir/mir_void_return.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
fn mir() -> (){
    let x = 1;
    let mut y = 0;
    while  y < x {
        y += 1
    }
}

pub fn main() {
    mir();
}


