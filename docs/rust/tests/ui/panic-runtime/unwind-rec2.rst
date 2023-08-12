tests/ui/panic-runtime/unwind-rec2.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:explicit panic
// ignore-emscripten no processes

fn build1() -> Vec<isize> {
    vec![0, 0, 0, 0, 0, 0, 0]
}

fn build2() -> Vec<isize> {
    panic!();
}

struct Blk {
    node: Vec<isize>,
    span: Vec<isize>,
}

fn main() {
    let _blk = Blk {
        node: build1(),
        span: build2(),
    };
}


