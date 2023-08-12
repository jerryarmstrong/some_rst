tests/ui/functions-closures/closure-bounds-can-capture-chan.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

use std::sync::mpsc::channel;

fn foo<F:FnOnce()+Send>(blk: F) {
    blk();
}

pub fn main() {
    let (tx, rx) = channel();
    foo(move || {
        tx.send(()).unwrap();
    });
    rx.recv().unwrap();
}


