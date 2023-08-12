tests/ui/statics/static-method-xcrate.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:static-methods-crate.rs

extern crate static_methods_crate;

use static_methods_crate::read;

pub fn main() {
    let result: isize = read("5".to_string());
    assert_eq!(result, 5);
    assert_eq!(read::readMaybe("false".to_string()), Some(false));
    assert_eq!(read::readMaybe("foo".to_string()), None::<bool>);
}


