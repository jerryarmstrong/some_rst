tests/ui/for-loop-while/loop-labeled-break-value.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

fn main() {
    'outer: loop {
        let _: i32 = loop { break 'outer };
    }
    'outer2: loop {
        let _: i32 = loop { loop { break 'outer2 } };
    }
}


