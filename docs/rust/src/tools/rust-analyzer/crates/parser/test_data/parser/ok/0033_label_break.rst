src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0033_label_break.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // format with label break value.
fn main() {
    'empty_block: {}

    'block: {
        do_thing();
        if condition_not_met() {
            break 'block;
        }
        do_next_thing();
        if condition_not_met() {
            break 'block;
        }
        do_last_thing();
    }

    let result = 'block: {
        if foo() {
            // comment
            break 'block 1;
        }
        if bar() {
            /* comment */
            break 'block 2;
        }
        3
    };
}


