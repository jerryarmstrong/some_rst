tests/ui/rfc-2457/extern_block_nonascii_forbidden.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(extern_types)]

extern "C" {
    type 一; //~ items in `extern` blocks cannot use non-ascii identifiers
    fn 二(); //~ items in `extern` blocks cannot use non-ascii identifiers
    static 三: usize; //~ items in `extern` blocks cannot use non-ascii identifiers
}

fn main() {}


