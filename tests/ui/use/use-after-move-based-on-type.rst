tests/ui/use/use-after-move-based-on-type.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x = "Hello!".to_string();
    let _y = x;
    println!("{}", x); //~ ERROR borrow of moved value
}


