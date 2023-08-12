tests/ui/array-slice-vec/vec-matching-fixed.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn a() {
    let x = [1, 2, 3];
    match x {
        [1, 2, 4] => unreachable!(),
        [0, 2, 3, ..] => unreachable!(),
        [0, .., 3] => unreachable!(),
        [0, ..] => unreachable!(),
        [1, 2, 3] => (),
        [_, _, _] => unreachable!(),
    }
    match x {
        [..] => (),
    }
    match x {
        [_, _, _, ..] => (),
    }
    match x {
        [a, b, c] => {
            assert_eq!(1, a);
            assert_eq!(2, b);
            assert_eq!(3, c);
        }
    }
}

pub fn main() {
    a();
}


