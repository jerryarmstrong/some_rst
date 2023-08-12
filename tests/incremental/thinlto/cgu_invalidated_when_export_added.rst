tests/incremental/thinlto/cgu_invalidated_when_export_added.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: cfail1 cfail2
// build-pass

// rust-lang/rust#69798:
//
// This is analogous to cgu_invalidated_when_import_added, but it covers a
// problem uncovered where a change to the *export* set caused a link failure
// when reusing post-LTO optimized object code.

pub struct Foo {}
impl Drop for Foo {
    fn drop(&mut self) {
        println!("Dropping Foo");
    }
}
#[no_mangle]
pub extern "C" fn run() {
    thread_local! { pub static FOO : Foo = Foo { } ; }

    #[cfg(cfail2)]
    {
        FOO.with(|_f| ())
    }
}

pub fn main() { run() }


