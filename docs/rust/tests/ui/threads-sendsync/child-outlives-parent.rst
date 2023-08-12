tests/ui/threads-sendsync/child-outlives-parent.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Reported as issue #126, child leaks the string.

// pretty-expanded FIXME #23616
// ignore-emscripten no threads support

use std::thread;

fn child2(_s: String) { }

pub fn main() {
    let _x = thread::spawn(move|| child2("hi".to_string()));
}


