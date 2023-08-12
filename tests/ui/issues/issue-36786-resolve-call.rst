tests/ui/issues/issue-36786-resolve-call.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Ensure that types that rely on obligations are autoderefed
// correctly

fn main() {
    let x : Vec<Box<dyn Fn()>> = vec![Box::new(|| ())];
    x[0]()
}


