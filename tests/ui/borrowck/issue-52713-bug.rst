tests/ui/borrowck/issue-52713-bug.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for a bug in #52713: this was an optimization for
// computing liveness that wound up accidentally causing the program
// below to be accepted.

fn foo<'a>(x: &'a mut u32) -> u32 {
    let mut x = 22;
    let y = &x;
    if false {
        return x;
    }

    x += 1; //~ ERROR
    println!("{}", y);
    return 0;
}

fn main() { }


