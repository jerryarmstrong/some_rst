src/tools/rustfmt/tests/source/file-lines-item.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-file_lines: [{"file":"tests/source/file-lines-item.rs","range":[6,8]}]

use foo::{c, b, a};
use bar;

fn foo() {
    bar ( ) ;
}

impl Drop for Context {
     fn drop(&mut self) {
    }
}

impl Bar for Baz {
    fn foo() {
        bar(
            baz, // Who knows?
        )
    }
}


