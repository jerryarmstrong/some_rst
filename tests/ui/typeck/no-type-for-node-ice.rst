tests/ui/typeck/no-type-for-node-ice.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Related issues: #20401, #20506, #20614, #20752, #20829, #20846, #20885, #20886

fn main() {
    "".homura[""]; //~ no field `homura` on type `&'static str`
}


