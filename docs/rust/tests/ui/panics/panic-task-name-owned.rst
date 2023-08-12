tests/ui/panics/panic-task-name-owned.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:thread 'owned name' panicked at 'test'
// ignore-emscripten Needs threads.

use std::thread::Builder;

fn main() {
    let r: () = Builder::new()
                    .name("owned name".to_string())
                    .spawn(move || {
                        panic!("test");
                        ()
                    })
                    .unwrap()
                    .join()
                    .unwrap();
    panic!();
}


