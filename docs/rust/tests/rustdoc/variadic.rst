tests/rustdoc/variadic.rs
=========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "C" {
    // @has variadic/fn.foo.html //pre 'pub unsafe extern "C" fn foo(x: i32, ...)'
    pub fn foo(x: i32, ...);
}


