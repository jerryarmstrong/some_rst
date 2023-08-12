tests/ui/structs/struct-missing-comma.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Issue #50636
// run-rustfix

pub struct S {
    pub foo: u32 //~ expected `,`, or `}`, found keyword `pub`
    //     ~^ HELP try adding a comma: ','
    pub bar: u32
}

fn main() {
    let _ = S { foo: 5, bar: 6 };
}


