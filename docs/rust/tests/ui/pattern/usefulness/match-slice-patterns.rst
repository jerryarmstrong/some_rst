tests/ui/pattern/usefulness/match-slice-patterns.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn check(list: &[Option<()>]) {
    match list {
    //~^ ERROR `&[_, Some(_), .., None, _]` not covered
        &[] => {},
        &[_] => {},
        &[_, _] => {},
        &[_, None, ..] => {},
        &[.., Some(_), _] => {},
    }
}

fn main() {}


