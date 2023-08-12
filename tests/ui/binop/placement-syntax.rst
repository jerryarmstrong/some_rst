tests/ui/binop/placement-syntax.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x = -5;
    if x<-1 { //~ ERROR unexpected token: `<-`
        println!("ok");
    }
}


