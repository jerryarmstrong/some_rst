src/tools/rustfmt/tests/target/issue_4943.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    impl SomeStruct {
    fn process<T>(v: T) -> <Self as GAT>::R<T>
    where
        Self: GAT<R<T> = T>,
    {
        SomeStruct::do_something(v)
    }
}


