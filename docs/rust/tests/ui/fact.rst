tests/ui/fact.rs
================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn f(x: isize) -> isize {
    // println!("in f:");

    println!("{}", x);
    if x == 1 {
        // println!("bottoming out");

        return 1;
    } else {
        // println!("recurring");

        let y: isize = x * f(x - 1);
        // println!("returned");

        println!("{}", y);
        return y;
    }
}

pub fn main() {
    assert_eq!(f(5), 120);
    // println!("all done");

}


