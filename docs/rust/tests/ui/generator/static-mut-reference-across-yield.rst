tests/ui/generator/static-mut-reference-across-yield.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
// revisions: mir thir
// [thir]compile-flags: -Zthir-unsafeck

#![feature(generators)]

static mut A: [i32; 5] = [1, 2, 3, 4, 5];

fn is_send_sync<T: Send + Sync>(_: T) {}

fn main() {
    unsafe {
        let gen_index = static || {
            let u = A[{
                yield;
                1
            }];
        };
        let gen_match = static || match A {
            i if {
                yield;
                true
            } =>
            {
                ()
            }
            _ => (),
        };
        is_send_sync(gen_index);
        is_send_sync(gen_match);
    }
}


