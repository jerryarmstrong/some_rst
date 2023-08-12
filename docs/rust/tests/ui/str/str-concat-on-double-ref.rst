tests/ui/str/str-concat-on-double-ref.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let a: &String = &"1".to_owned();
    let b: &str = &"2";
    let c = a + b;
    //~^ ERROR cannot add `&str` to `&String`
    println!("{:?}", c);
}


