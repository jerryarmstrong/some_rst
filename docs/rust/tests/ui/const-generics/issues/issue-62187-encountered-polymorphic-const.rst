tests/ui/const-generics/issues/issue-62187-encountered-polymorphic-const.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
pub trait BitLen: Sized {
    const BIT_LEN: usize;
}

impl<const L: usize> BitLen for [u8; L] {
    const BIT_LEN: usize = 8 * L;
}

fn main() {
    let _foo = <[u8; 2]>::BIT_LEN;
}


