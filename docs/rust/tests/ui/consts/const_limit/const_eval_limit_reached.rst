tests/ui/consts/const_limit/const_eval_limit_reached.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_eval_limit)]
#![const_eval_limit = "500"]

const X: usize = {
    let mut x = 0;
    while x != 1000 {
        //~^ ERROR evaluation of constant value failed
        x += 1;
    }

    x
};

fn main() {
    assert_eq!(X, 1000);
}


