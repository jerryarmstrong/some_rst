tests/ui/raw-ref-op/unusual_locations.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(raw_ref_op)]

const USES_PTR: () = { let u = (); &raw const u; };
static ALSO_USES_PTR: () = { let u = (); &raw const u; };

fn main() {
    let x: [i32; { let u = 2; let x = &raw const u; 4 }]
        = [2; { let v = 3; let y = &raw const v; 4 }];
    let mut one = 1;
    let two = 2;
    if &raw const one == &raw mut one {
        match &raw const two {
            _ => {}
        }
    }
    let three = 3;
    let mut four = 4;
    println!("{:p}", &raw const three);
    unsafe { &raw mut four; }
}


