src/tools/rustfmt/tests/target/issue-5009/5_nested_for_loop_with_connector_in_if_elseif_else.rs
===============================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let in_ = false;

    for variable_in_x /* ... */ in 0..1 {
        for variable_in_y /* ... */ in 0..1 {
            if in_ {

            } else if in_ {

            } else {

            }
        }
    }
}


