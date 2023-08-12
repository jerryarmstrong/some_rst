src/tools/clippy/tests/ui/crashes/auxiliary/ice-8681-aux.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn foo(x: &u32) -> u32 {
    /* Safety:
     * This is totally ok.
     */
    unsafe { *(x as *const u32) }
}


