tests/ui/moves/move-arg-2.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn test(foo: Box<Vec<isize>>) { assert_eq!((*foo)[0], 10); }

pub fn main() {
    let x = Box::new(vec![10]);
    // Test forgetting a local by move-in
    test(x);

    // Test forgetting a temporary by move-in.
    test(Box::new(vec![10]));
}


