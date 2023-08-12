tests/ui/lint/unused/unused-mut-warning-captured-var.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![forbid(unused_mut)]

fn main() {
    let mut x = 1;
    //~^ ERROR: variable does not need to be mutable
    (move|| { println!("{}", x); })();
}


