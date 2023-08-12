tests/ui/lazy-and-or.rs
=======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn incr(x: &mut isize) -> bool { *x += 1; assert!((false)); return false; }

pub fn main() {
    let x = 1 == 2 || 3 == 3;
    assert!((x));
    let mut y: isize = 10;
    println!("{}", x || incr(&mut y));
    assert_eq!(y, 10);
    if true && x { assert!((true)); } else { assert!((false)); }
}


