tests/ui/macros/macro-meta-items-modern.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

macro_rules! check { ($meta:meta) => () }

check!(meta(a b c d));
check!(meta[a b c d]);
check!(meta { a b c d });
check!(meta);
check!(meta = 0);

fn main() {}


