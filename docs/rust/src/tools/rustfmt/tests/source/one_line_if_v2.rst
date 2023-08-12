src/tools/rustfmt/tests/source/one_line_if_v2.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-version: Two

fn plain_if(x: bool) -> u8 {
    if x {
        0
    } else {
        1
    }
}

fn paren_if(x: bool) -> u8 {
    (if x { 0 } else { 1 })
}

fn let_if(x: bool) -> u8 {
    let x = if x {
        foo()
    } else {
        bar()
    };
    x
}

fn return_if(x: bool) -> u8 {
    return if x {
        0
    } else {
        1
    };
}

fn multi_if() {
    use std::io;
    if x { foo() } else { bar() }
    if x { foo() } else { bar() }
}

fn middle_if() {
    use std::io;
    if x { foo() } else { bar() }
    let x = 1;
}


