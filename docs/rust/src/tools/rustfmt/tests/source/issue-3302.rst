src/tools/rustfmt/tests/source/issue-3302.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-version: Two

macro_rules! moo1 {
    () => {
        bar! {
"
"
        }
    };
}

macro_rules! moo2 {
    () => {
        bar! {
        "
"
        }
    };
}

macro_rules! moo3 {
    () => {
        42
        /*
        bar! {
        "
        toto
tata"
        }
        */
    };
}

macro_rules! moo4 {
    () => {
        bar! {
"
    foo
        bar
baz"
        }
    };
}


