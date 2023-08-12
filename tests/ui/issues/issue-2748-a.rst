tests/ui/issues/issue-2748-a.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
#![allow(dead_code)]
#![allow(non_snake_case)]

// pretty-expanded FIXME #23616

struct CMap<'a> {
    buf: &'a [u8],
}

fn CMap(buf: &[u8]) -> CMap {
    CMap {
        buf: buf
    }
}

pub fn main() { }


