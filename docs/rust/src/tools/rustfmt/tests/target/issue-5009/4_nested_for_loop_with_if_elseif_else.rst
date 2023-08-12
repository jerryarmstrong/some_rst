src/tools/rustfmt/tests/target/issue-5009/4_nested_for_loop_with_if_elseif_else.rs
==================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    for variable_in_x /* ... */ in 0..1 {
        for variable_in_y /* ... */ in 0..1 {
            if false {

            } else if false {

            } else {

            }
        }
    }
}


