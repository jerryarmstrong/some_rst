tests/ui/label/label_break_value_unlabeled_break.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused_labels)]

// Simple unlabeled break should yield in an error
fn unlabeled_break_simple() {
    'b: {
        break; //~ ERROR unlabeled `break` inside of a labeled block
    }
}

// Unlabeled break that would cross a labeled block should yield in an error
fn unlabeled_break_crossing() {
    loop {
        'b: {
            break; //~ ERROR unlabeled `break` inside of a labeled block
        }
    }
}

pub fn main() {}


