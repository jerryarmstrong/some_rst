tests/ui/threads-sendsync/sendfn-is-a-block.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass


fn test<F>(f: F) -> usize where F: FnOnce(usize) -> usize {
    return f(22);
}

pub fn main() {
    let y = test(|x| 4 * x);
    assert_eq!(y, 88);
}


