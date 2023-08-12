tests/ui/bare-fn-implements-fn-mut.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use std::ops::FnMut;

fn call_f<F:FnMut()>(mut f: F) {
    f();
}

fn f() {
    println!("hello");
}

fn call_g<G:FnMut(String,String) -> String>(mut g: G, x: String, y: String)
          -> String {
    g(x, y)
}

fn g(mut x: String, y: String) -> String {
    x.push_str(&y);
    x
}

fn main() {
    call_f(f);
    assert_eq!(call_g(g, "foo".to_string(), "bar".to_string()),
               "foobar");
}


