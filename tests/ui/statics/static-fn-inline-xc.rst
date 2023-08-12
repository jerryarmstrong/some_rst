tests/ui/statics/static-fn-inline-xc.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:static_fn_inline_xc_aux.rs

// pretty-expanded FIXME #23616

extern crate static_fn_inline_xc_aux as mycore;

use mycore::num;

pub fn main() {
    let _1: f64 = num::Num2::from_int2(1);
}


