tests/ui/borrowck/move-in-pattern-mut-in-loop.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #80913.

fn main() {
    let mut x = 42_i32;
    let mut opt = Some(&mut x);
    for _ in 0..5 {
        if let Some(mut _x) = opt {}
        //~^ ERROR: use of moved value
    }
}


