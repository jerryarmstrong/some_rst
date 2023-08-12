tests/ui/rfcs/rfc-2005-default-binding-mode/tuple.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
pub fn main() {
    let foo = (Some(1), (), (), vec![2, 3]);

    match &foo {
        (Some(n), .., v) => {
            assert_eq!((*v).len(), 2);
            assert_eq!(*n, 1);
        }
        (None, (), (), ..) => panic!(),
    }
}


