src/tools/rustfmt/tests/target/file-lines-3.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-file_lines: [{"file":"tests/source/file-lines-3.rs","range":[4,8]},{"file":"tests/source/file-lines-3.rs","range":[10,15]}]

fn floaters() {
    let x = Foo {
        field1: val1,
        field2: val2,
    }
    .method_call()
    .method_call();

    let y = if cond { val1 } else { val2 }.method_call();

    {
        match x {
            PushParam => {
                // comment
                stack.push(mparams[match cur.to_digit(10) {
                                            Some(d) => d as usize - 1,
                                            None => return Err("bad param number".to_owned()),
                                        }]
                               .clone());
            }
        }
    }
}


