tests/ui/rfcs/rfc-2175-or-if-while-let/basic.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]

enum E {
    V(u8),
    U(u8),
    W,
}
use E::*;

fn main() {
    let mut e = V(10);

    if let V(x) | U(x) = e {
        assert_eq!(x, 10);
    }
    while let V(x) | U(x) = e {
        assert_eq!(x, 10);
        e = W;
    }

    // Accept leading `|`:

    let mut e = V(10);

    if let | V(x) | U(x) = e {
        assert_eq!(x, 10);
    }
    while let | V(x) | U(x) = e {
        assert_eq!(x, 10);
        e = W;
    }
}


