tests/ui/hashmap/hashmap-iter-value-lifetime.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let mut my_stuff = std::collections::HashMap::new();
    my_stuff.insert(0, 42);

    let (_, thing) = my_stuff.iter().next().unwrap();

    my_stuff.clear(); //~ ERROR cannot borrow

    println!("{}", *thing);
}


