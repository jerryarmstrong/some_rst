tests/ui/nll/assign-while-to-immutable.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // We used to incorrectly assign to `x` twice when generating MIR for this
// function, preventing this from compiling.

// check-pass

fn main() {
    let x = while false {
        break;
    };
    let y = 'l: while break 'l {};
}


