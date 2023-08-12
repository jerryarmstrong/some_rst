tests/ui/for-loop-while/liveness-loop-break.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
fn test() {
    let v;
    loop {
        v = 3;
        break;
    }
    println!("{}", v);
}

pub fn main() {
    test();
}


