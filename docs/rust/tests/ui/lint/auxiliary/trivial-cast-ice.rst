tests/ui/lint/auxiliary/trivial-cast-ice.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_export]
macro_rules! foo {
    () => {
        let x: &Option<i32> = &Some(1);
        let _y = x as *const Option<i32>;
    }
}


