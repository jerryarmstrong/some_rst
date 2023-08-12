tests/run-make-fulldeps/issue-68794-textrel-on-minimal-lib/foo.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "staticlib"]

#[no_mangle]
pub extern "C" fn foo(x: u32) {
    // using the println! makes it so that enough code from the standard
    // library is included (see issue #68794)
    println!("foo: {}", x);
}


