tests/ui/resolve/issue-104700-inner_scope.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let foo = 1;
    {
        let bar = 2;
        let test_func = |x| x > 3;
    }
    if bar == 2 { //~ ERROR cannot find value
        println!("yes");
    }
    test_func(1); //~ ERROR cannot find function
}


