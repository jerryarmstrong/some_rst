tests/ui/borrowck/issue-58776-borrowck-scans-children.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let mut greeting = "Hello world!".to_string();
    let res = (|| (|| &greeting)())();

    greeting = "DEALLOCATED".to_string();
    //~^ ERROR cannot assign
    drop(greeting);
    //~^ ERROR cannot move

    println!("thread result: {:?}", res);
}


