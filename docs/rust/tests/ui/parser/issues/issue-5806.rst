tests/ui/parser/issues/issue-5806.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // normalize-stderr-test: "parser:.*\(" -> "parser: $$ACCESS_DENIED_MSG ("
// normalize-stderr-test: "os error \d+" -> "os error $$ACCESS_DENIED_CODE"

#[path = "../parser"]
mod foo; //~ ERROR couldn't read

fn main() {}


