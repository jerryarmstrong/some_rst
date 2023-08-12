tests/ui/borrowck/borrowck-vec-pattern-move-tail.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let mut a = [1, 2, 3, 4];
    let t = match a {
        [1, 2, ref tail @ ..] => tail,
        _ => unreachable!()
    };
    println!("t[0]: {}", t[0]);
    a[2] = 0; //~ ERROR cannot assign to `a[_]` because it is borrowed
    println!("t[0]: {}", t[0]);
    t[0];
}


