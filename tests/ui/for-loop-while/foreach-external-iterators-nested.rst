tests/ui/for-loop-while/foreach-external-iterators-nested.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let x = [1; 100];
    let y = [2; 100];
    let mut p = 0;
    let mut q = 0;
    for i in &x[..] {
        for j in &y[..] {
            p += *j;
        }
        q += *i + p;
    }
    assert_eq!(q, 1010100);
}


