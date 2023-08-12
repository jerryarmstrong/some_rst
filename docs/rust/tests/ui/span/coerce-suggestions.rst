tests/ui/span/coerce-suggestions.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn test(_x: &mut String) {}

fn test2(_x: &mut i32) {}


fn main() {
    let x: usize = String::new();
    //~^ ERROR E0308
    let x: &str = String::new();
    //~^ ERROR E0308
    let y = String::new();
    test(&y);
    //~^ ERROR E0308
    test2(&y);
    //~^ ERROR E0308
    let f;
    f = Box::new(f);
    //~^ ERROR E0308

    let s = &mut String::new();
    s = format!("foo");
    //~^ ERROR E0308
}


