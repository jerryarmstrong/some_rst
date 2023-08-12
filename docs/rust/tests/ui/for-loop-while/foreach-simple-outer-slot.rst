tests/ui/for-loop-while/foreach-simple-outer-slot.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass



pub fn main() {
    let mut sum: isize = 0;
    first_ten(|i| { println!("main"); println!("{}", i); sum = sum + i; });
    println!("sum");
    println!("{}", sum);
    assert_eq!(sum, 45);
}

fn first_ten<F>(mut it: F) where F: FnMut(isize) {
    let mut i: isize = 0;
    while i < 10 { println!("first_ten"); it(i); i = i + 1; }
}


