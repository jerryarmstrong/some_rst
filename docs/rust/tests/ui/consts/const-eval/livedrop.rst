tests/ui/consts/const-eval/livedrop.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const _: Option<Vec<i32>> = {
    let mut never_returned = Some(Vec::new());
    let mut always_returned = None; //~ ERROR destructor of

    let mut i = 0;
    loop {
        always_returned = never_returned;
        never_returned = None;

        i += 1;
        if i == 10 {
            break always_returned;
        }
    }
};

fn main() {}


