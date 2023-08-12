tests/ui/array-slice-vec/repeated-vector-syntax.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let x = [ [true]; 512 ];
    let y = [ 0; 1 ];

    print!("[");
    for xi in &x[..] {
        print!("{:?}, ", &xi[..]);
    }
    println!("]");
    println!("{:?}", &y[..]);
}


