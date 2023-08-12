tests/ui/for-loop-while/liveness-assign-imm-local-after-loop.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(unused_assignments)]
// pretty-expanded FIXME #23616

#![allow(unreachable_code)]
#![allow(unused_variables)]

fn test(_cond: bool) {
    let v: isize;
    v = 1;
    loop { } // loop never terminates, so no error is reported
    v = 2;
}

pub fn main() {
    // note: don't call test()... :)
}


