tests/ui/regions/regions-close-over-type-parameter-successfully.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// A test where we (successfully) close over a reference into
// an object.

trait SomeTrait { fn get(&self) -> isize; }

impl<'a> SomeTrait for &'a isize {
    fn get(&self) -> isize {
        **self
    }
}

fn make_object<'a,A:SomeTrait+'a>(v: A) -> Box<dyn SomeTrait+'a> {
    Box::new(v) as Box<dyn SomeTrait+'a>
}

fn main() {
    let i: isize = 22;
    let obj = make_object(&i);
    assert_eq!(22, obj.get());
}


