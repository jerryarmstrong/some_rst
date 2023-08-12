tests/ui/issues/issue-2463.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

struct Pair { f: isize, g: isize }

pub fn main() {

    let x = Pair {
        f: 0,
        g: 0,
    };

    let _y = Pair {
        f: 1,
        g: 1,
        .. x
    };

    let _z = Pair {
        f: 1,
        .. x
    };

}


