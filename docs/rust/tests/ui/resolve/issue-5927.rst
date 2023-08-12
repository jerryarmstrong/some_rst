tests/ui/resolve/issue-5927.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let z = match 3 {
        x(1) => x(1) //~ ERROR cannot find tuple struct or tuple variant `x` in this scope
        //~^ ERROR cannot find function `x` in this scope
    };
    assert!(z == 3);
}


