tests/ui/for-loop-while/foreach-external-iterators-break.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let x = [1; 100];
    let mut y = 0;
    for i in &x[..] {
        if y > 10 {
            break;
        }
        y += *i;
    }
    assert_eq!(y, 11);
}


