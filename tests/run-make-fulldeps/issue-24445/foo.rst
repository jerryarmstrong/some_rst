tests/run-make-fulldeps/issue-24445/foo.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "staticlib"]

struct Destroy;
impl Drop for Destroy {
    fn drop(&mut self) { println!("drop"); }
}

thread_local! {
    static X: Destroy = Destroy
}

#[no_mangle]
pub extern "C" fn foo() {
    X.with(|_| ());
}


