tests/ui/consts/issue-39161-bogus-error.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

pub struct X {
    pub a: i32,
    pub b: i32,
}

fn main() {
    const DX: X = X { a: 0, b: 0 };
    const _X1: X = X { a: 1, ..DX };
    let _x2 = X { a: 1, b: 2, ..DX };
    const _X3: X = X { a: 1, b: 2, ..DX };
}


