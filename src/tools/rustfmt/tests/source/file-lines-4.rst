src/tools/rustfmt/tests/source/file-lines-4.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-file_lines: []
// (Test that nothing is formatted if an empty array is specified.)

fn floaters() {
    let x = Foo {
                field1: val1,
                field2: val2,
            }
            .method_call().method_call();

    let y = if cond {
                val1
            } else {
                val2	
            }
                .method_call();
                                                                                              // aaaaaaaaaaaaa
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


