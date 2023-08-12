tests/ui/issues/issue-2550.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(non_snake_case)]

// pretty-expanded FIXME #23616

struct C {
    x: usize,
}

fn C(x: usize) -> C {
    C {
        x: x
    }
}

fn f<T>(_x: T) {
}

pub fn main() {
    f(C(1));
}


