tests/ui/dropck/drop-with-active-borrows-1.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let a = "".to_string();
    let b: Vec<&str> = a.lines().collect();
    drop(a);    //~ ERROR cannot move out of `a` because it is borrowed
    for s in &b {
        println!("{}", *s);
    }
}


