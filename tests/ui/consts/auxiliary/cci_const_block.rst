tests/ui/consts/auxiliary/cci_const_block.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub static BLOCK_FN_DEF: fn(usize) -> usize = {
    fn foo(a: usize) -> usize {
        a + 10
    }
    foo
};


