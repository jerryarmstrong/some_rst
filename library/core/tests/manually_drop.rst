library/core/tests/manually_drop.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use core::mem::ManuallyDrop;

#[test]
fn smoke() {
    #[derive(Clone)]
    struct TypeWithDrop;
    impl Drop for TypeWithDrop {
        fn drop(&mut self) {
            unreachable!("Should not get dropped");
        }
    }

    let x = ManuallyDrop::new(TypeWithDrop);
    drop(x);

    // also test unsizing
    let x: Box<ManuallyDrop<[TypeWithDrop]>> =
        Box::new(ManuallyDrop::new([TypeWithDrop, TypeWithDrop]));
    drop(x);

    // test clone and clone_from implementations
    let mut x = ManuallyDrop::new(TypeWithDrop);
    let y = x.clone();
    x.clone_from(&y);
    drop(x);
    drop(y);
}


