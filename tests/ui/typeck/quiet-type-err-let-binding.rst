tests/ui/typeck/quiet-type-err-let-binding.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // fn foo() -> String {
//    String::new()
// }

fn test(s: &str) {
    println!("{}", s);
}

fn test2(s: String) {
    println!("{}", s);
}

fn main() {
    let x = foo(); //~ERROR cannot find function `foo` in this scope
    test(&x);
    test2(x); // Does not complain about `x` being a `&str`.
}


