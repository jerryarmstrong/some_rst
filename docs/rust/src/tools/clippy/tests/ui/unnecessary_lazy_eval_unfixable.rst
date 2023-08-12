src/tools/clippy/tests/ui/unnecessary_lazy_eval_unfixable.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::unnecessary_lazy_evaluations)]

struct Deep(Option<usize>);

#[derive(Copy, Clone)]
struct SomeStruct {
    some_field: usize,
}

fn main() {
    // fix will break type inference
    let _ = Ok(1).unwrap_or_else(|()| 2);
    mod e {
        pub struct E;
    }
    let _ = Ok(1).unwrap_or_else(|e::E| 2);
    let _ = Ok(1).unwrap_or_else(|SomeStruct { .. }| 2);

    // Fix #6343
    let arr = [(Some(1),)];
    Some(&0).and_then(|&i| arr[i].0);
}


