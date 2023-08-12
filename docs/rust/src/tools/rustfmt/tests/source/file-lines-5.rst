src/tools/rustfmt/tests/source/file-lines-5.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-file_lines: [{"file":"tests/source/file-lines-5.rs","range":[3,5]}]

struct A {
t: i64,     
}

mod foo {
    fn bar() {
                         // test
                             let i = 12;
                                 // test
    }
    // aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    fn baz() {
        let j = 15;     
    }
}


