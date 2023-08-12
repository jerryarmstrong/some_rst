tests/ui/issues/issue-3424.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![allow(dead_code)]
#![allow(non_camel_case_types)]
// rustc --test ignores2.rs && ./ignores2

pub struct Path;

type rsrc_loader = Box<dyn FnMut(&Path) -> Result<String, String>>;

fn tester()
{
    let mut loader: rsrc_loader = Box::new(move |_path| {
        Ok("more blah".to_string())
    });

    let path = Path;
    assert!(loader(&path).is_ok());
}

pub fn main() {}


