tests/run-make/coverage/loop_break_value.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused_assignments, unused_variables)]

fn main() {
    let result
        =
            loop
        {
            break
            10
            ;
        }
    ;
}


