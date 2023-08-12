tests/ui/borrowck/issue-54597-reject-move-out-of-borrow-via-pat.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code)]

#[derive(Debug)]
struct Value;
impl Value {
    fn as_array(&self) -> Option<&Vec<Value>> {
        None
    }
}

fn foo(val: Value) {
    let _reviewers_original: Vec<Value> = match val.as_array() {
        Some(array) => {
            *array //~ ERROR cannot move out of `*array`
        }
        None => vec![]
    };
}

fn main() { }


