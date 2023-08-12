tests/ui/closures/old-closure-explicit-types.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    fn as_buf<T, F>(s: String, f: F) -> T where F: FnOnce(String) -> T { f(s) }
    as_buf("foo".to_string(), |foo: String| -> () { println!("{}", foo) });
}


