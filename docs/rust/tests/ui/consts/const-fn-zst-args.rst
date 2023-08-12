tests/ui/consts/const-fn-zst-args.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass

// Check that the evaluation of const-functions with
// zero-sized types as arguments compiles successfully

struct Zst {}

const fn foo(val: Zst) -> Zst { val }

const FOO: Zst = foo(Zst {});

fn main() {
    const _: Zst = FOO;
}


