tests/ui/async-await/issues/issue-66695-static-refs.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
// edition:2018

static A: [i32; 5] = [1, 2, 3, 4, 5];

async fn fun() {
    let u = A[async { 1 }.await];
    match A {
        i if async { true }.await => (),
        _ => (),
    }
}

fn main() {
    async {
        let u = A[async { 1 }.await];
    };
    async {
        match A {
            i if async { true }.await => (),
            _ => (),
        }
    };
}


