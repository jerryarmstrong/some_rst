tests/ui/for-loop-while/foreach-external-iterators-loop.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let x = [1; 100];
    let mut y = 0;
    for (n,i) in x.iter().enumerate() {
        if n < 10 {
            continue;
        }
        y += *i;
    }
    assert_eq!(y, 90);
}


