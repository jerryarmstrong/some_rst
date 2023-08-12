src/tools/clippy/tests/ui/auxiliary/implicit_hasher_macros.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_export]
macro_rules! implicit_hasher_fn {
    () => {
        pub fn f(input: &HashMap<u32, u32>) {}
    };
}


