tests/ui/array-slice-vec/copy-out-of-array-1.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// Ensure that we can copy out of a fixed-size array.
//
// (Compare with ui/moves/move-out-of-array-1.rs)

#[derive(Copy, Clone)]
struct C { _x: u8 }

fn main() {
    fn d() -> C { C { _x: 0 } }

    let _d1 = foo([d(), d(), d(), d()], 1);
    let _d3 = foo([d(), d(), d(), d()], 3);
}

fn foo(a: [C; 4], i: usize) -> C {
    a[i]
}


