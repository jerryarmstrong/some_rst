src/tools/miri/tests/pass/move-arg-2-unique.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(box_syntax)]

fn test(foo: Box<Vec<isize>>) {
    assert_eq!((*foo)[0], 10);
}

pub fn main() {
    let x = box vec![10];
    // Test forgetting a local by move-in
    test(x);
}


