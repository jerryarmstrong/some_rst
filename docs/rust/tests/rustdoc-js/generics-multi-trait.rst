tests/rustdoc-js/generics-multi-trait.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait SomeTrait {}
pub trait Zzzzzzzzzzzzzzzzzz {}

pub fn bet<Nonononononononono: SomeTrait + Zzzzzzzzzzzzzzzzzz>() -> Result<Nonononononononono, ()> {
    loop {}
}

pub fn beta<Nonononononononono: SomeTrait + Zzzzzzzzzzzzzzzzzz>(
    _param: Result<Nonononononononono, ()>,
) {
    loop {}
}


