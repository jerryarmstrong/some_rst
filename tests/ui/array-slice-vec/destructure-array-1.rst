tests/ui/array-slice-vec/destructure-array-1.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// Ensure that we can do a destructuring bind of a fixed-size array,
// even when the element type has a destructor.

struct D { x: u8 }

impl Drop for D { fn drop(&mut self) { } }

fn main() {
    fn d(x: u8) -> D { D { x: x } }

    let d1 = foo([d(1), d(2), d(3), d(4)], 1);
    let d3 = foo([d(5), d(6), d(7), d(8)], 3);
    assert_eq!(d1.x, 2);
    assert_eq!(d3.x, 8);
}

fn foo([a, b, c, d]: [D; 4], i: usize) -> D {
    match i {
        0 => a,
        1 => b,
        2 => c,
        3 => d,
        _ => panic!("unmatched"),
    }
}


