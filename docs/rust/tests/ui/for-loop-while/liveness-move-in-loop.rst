tests/ui/for-loop-while/liveness-move-in-loop.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]

// pretty-expanded FIXME #23616

fn take(x: isize) -> isize {x}

fn the_loop() {
    let mut list = Vec::new();
    loop {
        let x = 5;
        if x > 3 {
            list.push(take(x));
        } else {
            break;
        }
    }
}

pub fn main() {}


