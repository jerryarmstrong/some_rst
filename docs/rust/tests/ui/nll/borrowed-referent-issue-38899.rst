tests/ui/nll/borrowed-referent-issue-38899.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #38899

pub struct Block<'a> {
    current: &'a u8,
    unrelated: &'a u8,
}

fn bump<'a>(mut block: &mut Block<'a>) {
    let x = &mut block;
    println!("{}", x.current);
    let p: &'a u8 = &*block.current;
    //~^ ERROR cannot borrow `*block.current` as immutable because it is also borrowed as mutable
    drop(x);
    drop(p);
}

fn main() {}


