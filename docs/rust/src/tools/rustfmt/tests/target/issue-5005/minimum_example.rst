src/tools/rustfmt/tests/target/issue-5005/minimum_example.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(more_qualified_paths)]
macro_rules! show {
    ($ty:ty, $ex:expr) => {
        match $ex {
            <$ty>::A(_val) => println!("got a"), // formatting should not remove <$ty>::
            <$ty>::B => println!("got b"),
        }
    };
}


