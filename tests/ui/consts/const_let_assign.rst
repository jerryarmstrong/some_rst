tests/ui/consts/const_let_assign.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

struct S(i32);

const A: () = {
    let mut s = S(0);
    s.0 = 1;
};

fn main() {}


