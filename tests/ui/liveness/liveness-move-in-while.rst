tests/ui/liveness/liveness-move-in-while.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {

    let y: Box<isize> = 42.into();
    let mut x: Box<isize>;

    loop {
        println!("{}", y); //~ ERROR borrow of moved value: `y`
        while true { while true { while true { x = y; x.clone(); } } }
        //~^ WARN denote infinite loops with
        //~| WARN denote infinite loops with
        //~| WARN denote infinite loops with
    }
}


