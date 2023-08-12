tests/ui/union/union-macro.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// revisions: mirunsafeck thirunsafeck
// [thirunsafeck]compile-flags: -Z thir-unsafeck

#![allow(unused_variables)]

macro_rules! duplicate {
   ($i: item) => {
        mod m1 {
            $i
        }
        mod m2 {
            $i
        }
   }
}

duplicate! {
    pub union U {
        pub a: u8
    }
}

fn main() {
    let u1 = m1::U { a: 0 };
    let u2 = m2::U { a: 0 };
}


