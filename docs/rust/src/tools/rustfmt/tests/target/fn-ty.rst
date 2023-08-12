src/tools/rustfmt/tests/target/fn-ty.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f(
    xxxxxxxxxxxxxxxxxx: fn(a, b, b) -> a,
    xxxxxxxxxxxxxxxxxx: fn() -> a,
    xxxxxxxxxxxxxxxxxx: fn(a, b, b),
    xxxxxxxxxxxxxxxxxx: fn(),
    xxxxxxxxxxxxxxxxxx: fn(a, b, b) -> !,
    xxxxxxxxxxxxxxxxxx: fn() -> !,
) where
    F1: Fn(a, b, b) -> a,
    F2: Fn(a, b, b),
    F3: Fn(),
    F4: Fn() -> u32,
{
}


