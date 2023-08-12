tests/ui/test-attrs/test-runner-hides-buried-main.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags: --test

#![feature(rustc_attrs)]

#![allow(dead_code)]

mod a {
    fn b() {
        (|| {
            #[rustc_main]
            fn c() { panic!(); }
        })();
    }
}


