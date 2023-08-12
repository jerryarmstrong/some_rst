tests/ui/borrowck/borrowck-vec-pattern-tail-element-loan.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn a<'a>() -> &'a isize {
    let vec = vec![1, 2, 3, 4];
    let vec: &[isize] = &vec;
    let tail = match vec {
        &[_a, ref tail @ ..] => &tail[0],
        _ => panic!("foo")
    };
    tail //~ ERROR cannot return value referencing local variable `vec`
}

fn main() {
    let fifth = a();
    println!("{}", *fifth);
}


