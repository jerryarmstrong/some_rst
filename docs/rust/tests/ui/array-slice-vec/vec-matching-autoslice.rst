tests/ui/array-slice-vec/vec-matching-autoslice.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(illegal_floating_point_literal_pattern)] // FIXME #41620

pub fn main() {
    let x = [1, 2, 3];
    match x {
        [2, _, _] => panic!(),
        [1, a, b] => {
            assert_eq!([a, b], [2, 3]);
        }
        [_, _, _] => panic!(),
    }

    let y = ([(1, true), (2, false)], 0.5f64);
    match y {
        ([(1, a), (b, false)], _) => {
            assert_eq!(a, true);
            assert_eq!(b, 2);
        }
        ([_, _], 0.5) => panic!(),
        ([_, _], _) => panic!(),
    }
}


