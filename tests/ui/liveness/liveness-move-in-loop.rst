tests/ui/liveness/liveness-move-in-loop.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {

    let y: Box<isize> = 42.into();
    let mut x: Box<isize>;

    loop {
        println!("{}", y);
        loop {
            loop {
                loop {
                    x = y; //~ ERROR use of moved value
                    x.clone();
                }
            }
        }
    }
}


