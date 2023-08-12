tests/ui/consts/const-eval/promote-static.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // regression test for #67609.

// check-pass

static NONE: Option<String> = None;

static NONE_REF_REF: &&Option<String> = {
    let x = &&NONE;
    x
};

fn main() {
    println!("{:?}", NONE_REF_REF);
}


